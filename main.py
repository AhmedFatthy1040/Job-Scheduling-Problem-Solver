#!/usr/bin/env python3
"""
Job Scheduling Problem Solver

This module provides both GUI and CLI interfaces for solving job scheduling problems
using backtracking and genetic algorithms.
"""

import sys
import argparse
import tkinter as tk
from gui.main_window import MainWindow
from models.resource import Resource
from models.job import Job
from models.job_scheduling_problem import JobSchedulingProblem
from algorithms.backtracking_algorithm import BacktrackingAlgorithm
from algorithms.genetic_algorithm import GeneticAlgorithm
from utils.random_generator import RandomGenerator
from utils.scheduler_evaluator import SchedulerEvaluator


def run_cli_comparison():
    """Run algorithm comparison via command line interface."""
    print("Job Scheduling Problem Solver - Algorithm Comparison")
    print("=" * 60)
    
    instances = []
    total_backtracking = 0
    total_genetic = 0
    
    for instance_id in range(1, 6):
        print(f"\nGenerating Instance {instance_id}...")
        jobs = [RandomGenerator.generate_random_job(job_id) for job_id in range(1, 6)]
        resources = [RandomGenerator.generate_random_resource(resource_id) for resource_id in range(1, 4)]
        
        problem_instance = JobSchedulingProblem(jobs, resources)
        instances.append(problem_instance)
        
        print("Jobs:")
        for job in jobs:
            dependency_str = f"Job {job.dependency}" if job.dependency else "None"
            print(f"  Job {job.job_id}: Processing Time {job.processing_time}, Dependency {dependency_str}")
        
        print("Resources:")
        for resource in resources:
            print(f"  Resource {resource.resource_id}: Capacity {resource.capacity}")
    
    print(f"\n{'='*60}")
    print("Running Algorithms...")
    print("=" * 60)
    
    for i, instance in enumerate(instances, 1):
        print(f"\nEvaluating Instance {i}...")
        evaluator = SchedulerEvaluator(instance)
        evaluator.run_algorithms()
        comparison_results, avg_backtracking_time, avg_genetic_time = evaluator.evaluate_performance()
        
        for result in comparison_results:
            if result == 0:
                print("  → Backtracking Algorithm found better solution")
                total_backtracking += 1
            elif result == 1:
                print("  → Genetic Algorithm found better solution")
                total_genetic += 1
            elif result == 2:
                print("  → Both algorithms found equivalent solutions")
        
        print(f"  Avg Backtracking Time: {avg_backtracking_time:.6f} seconds")
        print(f"  Avg Genetic Time: {avg_genetic_time:.6f} seconds")
    
    print(f"\n{'='*60}")
    print("FINAL RESULTS")
    print("=" * 60)
    
    if total_backtracking > total_genetic:
        print("Overall Winner: Backtracking Algorithm")
    elif total_backtracking < total_genetic:
        print("Overall Winner: Genetic Algorithm")
    else:
        print("Overall Result: Tie between both algorithms")
    
    print(f"Backtracking wins: {total_backtracking}")
    print(f"Genetic wins: {total_genetic}")


def run_gui():
    """Run the graphical user interface."""
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()


def main():
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(
        description="Job Scheduling Problem Solver",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py              # Run GUI version
  python main.py --cli         # Run CLI comparison
  python main.py --gui         # Explicitly run GUI version
        """
    )
    
    parser.add_argument(
        '--cli', 
        action='store_true', 
        help='Run command line interface for algorithm comparison'
    )
    
    parser.add_argument(
        '--gui', 
        action='store_true', 
        help='Run graphical user interface (default)'
    )
    
    args = parser.parse_args()
    
    try:
        if args.cli:
            run_cli_comparison()
        else:
            run_gui()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()