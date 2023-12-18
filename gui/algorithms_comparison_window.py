import tkinter as tk
from tkinter import ttk
from models.resource import Resource
from models.job import Job
from models.job_scheduling_problem import JobSchedulingProblem
from utils.scheduler_evaluator import SchedulerEvaluator
from utils.random_generator import RandomGenerator

class AlgorithmComparisonWindow:
    def __init__(self, master):
        self.master = master
        master.title("Algorithm Comparison")

        self.random_button = tk.Button(master, text="Random", command=self.run_comparison)
        self.random_button.pack(pady=10)

        self.separator1 = ttk.Separator(master, orient="horizontal")
        self.separator1.pack(fill="x", pady=10)

        self.result_label = tk.Label(master, text="", font=("Helvetica", 12, "bold"))
        self.result_label.pack()

        self.instances_scrollbar = ttk.Scrollbar(master)
        self.instances_scrollbar.pack(side="right", fill="y")

        self.instances_text = tk.Text(master, wrap="none", height=25, width=50, yscrollcommand=self.instances_scrollbar.set)
        self.instances_text.pack(pady=10)

        self.instances_scrollbar.config(command=self.instances_text.yview)

    def run_comparison(self):
        instances = []
        total_backtracking = 0
        total_genetic = 0
        total_backtracking_time = 0
        total_genetic_time = 0

        instances_text = "Random Instances:\n"
        for instance_id in range(1, 6):
            jobs = [RandomGenerator.generate_random_job(job_id) for job_id in range(1, 6)]
            resources = [RandomGenerator.generate_random_resource(resource_id) for resource_id in range(1, 4)]

            problem_instance = JobSchedulingProblem(jobs, resources)
            instances.append(problem_instance)

            instances_text += f"Instance {instance_id}:\n"
            for job in jobs:
                instances_text += f"  Job {job.job_id}: Processing Time {job.processing_time}, Dependency {job.dependency}\n"
            for resource in resources:
                instances_text += f"  Resource {resource.resource_id}: Capacity {resource.capacity}\n"
            instances_text += "\n"

        self.instances_text.delete(1.0, tk.END)
        self.instances_text.insert(tk.END, instances_text)

        for instance in instances:
            evaluator = SchedulerEvaluator(instance)
            evaluator.run_algorithms()
            comparison_results, avg_backtracking_time, avg_genetic_time = evaluator.evaluate_performance()

            for result in comparison_results:
                if result == 0:
                    total_backtracking += 1
                elif result == 1:
                    total_genetic += 1

            total_backtracking_time += avg_backtracking_time
            total_genetic_time += avg_genetic_time

        avg_backtracking_time = total_backtracking_time / len(instances)
        avg_genetic_time = total_genetic_time / len(instances)

        result_label_text = ""
        if total_backtracking > total_genetic:
            result_label_text = "On average, Backtracking Algorithm is faster."
        elif total_backtracking < total_genetic:
            result_label_text = "On average, Genetic Algorithm is faster."
        else:
            result_label_text = "On average, both algorithms have the same performance."

        result_label_text += f"\nAvg Backtracking Time: {avg_backtracking_time:.6f} seconds"
        result_label_text += f"\nAvg Genetic Time: {avg_genetic_time:.6f} seconds"

        self.instances_text.delete(1.0, tk.END)
        self.instances_text.insert(tk.END, instances_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = AlgorithmComparisonWindow(root)
    root.geometry("600x600")
    root.mainloop()
