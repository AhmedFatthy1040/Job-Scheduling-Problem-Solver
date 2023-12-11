import tkinter as tk
from tkinter import messagebox
from gui.main_window import MainWindow
from models.job import Job
from models.resource import Resource
from models.job_scheduling_problem import JobSchedulingProblem
from algorithms.backtracking_algorithm import BacktrackingAlgorithm
from algorithms.genetic_algorithm import GeneticAlgorithm

class ResultWindow:
    def __init__(self, root, algorithm, problem_instance):
        self.root = root
        self.algorithm = algorithm
        self.problem_instance = problem_instance

        self.result_text = tk.Text(root, wrap=tk.WORD, height=20, width=60)
        self.result_text.grid(row=0, column=0, padx=10, pady=10)

        self.display_results()

    def display_results(self):
        if isinstance(self.algorithm, BacktrackingAlgorithm):
            self.algorithm.solve()
            self.display_schedule(self.algorithm.best_schedule)
        elif isinstance(self.algorithm, GeneticAlgorithm):
            self.algorithm.evolve()
            best_schedule = min(self.algorithm.population, key=lambda x: self.algorithm.fitness(x))
            self.display_schedule(best_schedule)

    def display_schedule(self, schedule):
        self.result_text.delete("1.0", tk.END)  # Clear the text widget before displaying results
        self.result_text.insert(tk.END, "Optimal Schedule:\n")

        if schedule is None:
            self.result_text.insert(tk.END, "No valid schedule found.\n")
            return

        resource_occupancy = {resource.resource_id: 0 for resource in self.problem_instance.resources}
        job_start_times = {job.job_id: 0 for job in self.problem_instance.jobs}

        for assignment in schedule:
            job = assignment[0]
            resource = assignment[1]

            dependency_start_time = job_start_times[job.dependency] if job.dependency is not None else 0
            start_time = max(resource_occupancy[resource.resource_id], dependency_start_time)
            end_time = start_time + job.processing_time

            result_line = (
                f"Job {job.job_id} scheduled on Resource {resource.resource_id} "
                f"Start Time: {start_time}, End Time: {end_time}\n"
            )
            self.result_text.insert(tk.END, result_line)

            resource_occupancy[resource.resource_id] = end_time
            job_start_times[job.job_id] = end_time
