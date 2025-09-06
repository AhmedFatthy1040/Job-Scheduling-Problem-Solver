#!/usr/bin/env python3
"""
Unit tests for the Job Scheduling Problem Solver.

This module contains tests for the core functionality of the scheduling algorithms.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models.job import Job
from models.resource import Resource
from models.job_scheduling_problem import JobSchedulingProblem
from algorithms.backtracking_algorithm import BacktrackingAlgorithm
from algorithms.genetic_algorithm import GeneticAlgorithm
from utils.random_generator import RandomGenerator


class TestJob(unittest.TestCase):
    """Test cases for the Job class."""
    
    def test_job_creation(self):
        """Test job creation with valid parameters."""
        job = Job(1, 5, None)
        self.assertEqual(job.job_id, 1)
        self.assertEqual(job.processing_time, 5)
        self.assertIsNone(job.dependency)
    
    def test_job_with_dependency(self):
        """Test job creation with dependency."""
        job = Job(2, 3, 1)
        self.assertEqual(job.dependency, 1)
    
    def test_job_invalid_processing_time(self):
        """Test that invalid processing time raises ValueError."""
        with self.assertRaises(ValueError):
            Job(1, 0, None)
        
        with self.assertRaises(ValueError):
            Job(1, -1, None)
    
    def test_job_self_dependency(self):
        """Test that self-dependency raises ValueError."""
        with self.assertRaises(ValueError):
            Job(1, 5, 1)


class TestResource(unittest.TestCase):
    """Test cases for the Resource class."""
    
    def test_resource_creation(self):
        """Test resource creation with valid parameters."""
        resource = Resource(1, 10)
        self.assertEqual(resource.resource_id, 1)
        self.assertEqual(resource.capacity, 10)
    
    def test_resource_invalid_capacity(self):
        """Test that invalid capacity raises ValueError."""
        with self.assertRaises(ValueError):
            Resource(1, 0)
        
        with self.assertRaises(ValueError):
            Resource(1, -5)


class TestJobSchedulingProblem(unittest.TestCase):
    """Test cases for the JobSchedulingProblem class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.jobs = [
            Job(1, 3, None),
            Job(2, 2, 1),
            Job(3, 4, None)
        ]
        self.resources = [
            Resource(1, 10),
            Resource(2, 8)
        ]
        self.problem = JobSchedulingProblem(self.jobs, self.resources)
    
    def test_problem_creation(self):
        """Test problem instance creation."""
        self.assertEqual(len(self.problem.jobs), 3)
        self.assertEqual(len(self.problem.resources), 2)


class TestBacktrackingAlgorithm(unittest.TestCase):
    """Test cases for the BacktrackingAlgorithm class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.jobs = [
            Job(1, 3, None),
            Job(2, 2, 1),
            Job(3, 4, None)
        ]
        self.resources = [
            Resource(1, 15),
            Resource(2, 10)
        ]
        self.problem = JobSchedulingProblem(self.jobs, self.resources)
        self.algorithm = BacktrackingAlgorithm(self.problem)
    
    def test_valid_schedule_check(self):
        """Test schedule validation."""
        valid_schedule = [
            (self.jobs[0], self.resources[0]),
            (self.jobs[1], self.resources[0]),
            (self.jobs[2], self.resources[1])
        ]
        self.assertTrue(self.algorithm.is_valid_schedule(valid_schedule))
        
        invalid_schedule = [
            (self.jobs[1], self.resources[0]),
        ]
        self.assertFalse(self.algorithm.is_valid_schedule(invalid_schedule))
    
    def test_solve_simple_problem(self):
        """Test solving a simple problem."""
        solution = self.algorithm.solve()
        self.assertIsNotNone(solution)
        self.assertTrue(self.algorithm.is_valid_schedule(solution))


class TestGeneticAlgorithm(unittest.TestCase):
    """Test cases for the GeneticAlgorithm class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.jobs = [
            Job(1, 3, None),
            Job(2, 2, 1),
            Job(3, 4, None)
        ]
        self.resources = [
            Resource(1, 15),
            Resource(2, 10)
        ]
        self.problem = JobSchedulingProblem(self.jobs, self.resources)
        self.algorithm = GeneticAlgorithm(self.problem, population_size=10, generations=5)
    
    def test_random_schedule_generation(self):
        """Test random schedule generation."""
        schedule = self.algorithm.generate_random_schedule()
        self.assertEqual(len(schedule), len(self.jobs))
        
        job_ids = [assignment[0].job_id for assignment in schedule]
        expected_ids = [job.job_id for job in self.jobs]
        self.assertEqual(sorted(job_ids), sorted(expected_ids))
    
    def test_population_initialization(self):
        """Test population initialization."""
        self.algorithm.initialize_population()
        self.assertEqual(len(self.algorithm.population), self.algorithm.population_size)
    
    def test_fitness_calculation(self):
        """Test fitness calculation."""
        schedule = self.algorithm.generate_random_schedule()
        fitness = self.algorithm.fitness(schedule)
        self.assertIsInstance(fitness, (int, float))
        self.assertGreaterEqual(fitness, 0)


class TestRandomGenerator(unittest.TestCase):
    """Test cases for the RandomGenerator class."""
    
    def test_generate_random_job(self):
        """Test random job generation."""
        job = RandomGenerator.generate_random_job(1)
        self.assertEqual(job.job_id, 1)
        self.assertGreater(job.processing_time, 0)
        self.assertLessEqual(job.processing_time, 10)
    
    def test_generate_random_resource(self):
        """Test random resource generation."""
        resource = RandomGenerator.generate_random_resource(1)
        self.assertEqual(resource.resource_id, 1)
        self.assertGreaterEqual(resource.capacity, 3)
        self.assertLessEqual(resource.capacity, 20)


class TestIntegration(unittest.TestCase):
    """Integration tests for the complete system."""
    
    def test_solve_with_both_algorithms(self):
        """Test solving the same problem with both algorithms."""
        jobs = [
            Job(1, 2, None),
            Job(2, 3, 1),
            Job(3, 1, None)
        ]
        resources = [
            Resource(1, 10),
            Resource(2, 8)
        ]
        problem = JobSchedulingProblem(jobs, resources)
        
        backtrack_algo = BacktrackingAlgorithm(problem)
        backtrack_solution = backtrack_algo.solve()
        
        genetic_algo = GeneticAlgorithm(problem, population_size=20, generations=10)
        genetic_solution = genetic_algo.evolve()
        
        if backtrack_solution:
            self.assertTrue(backtrack_algo.is_valid_schedule(backtrack_solution))
        
        if genetic_solution:
            self.assertTrue(genetic_algo.is_valid_schedule(genetic_solution))


def run_tests():
    """Run all tests."""
    unittest.main(verbosity=2)


if __name__ == '__main__':
    run_tests()