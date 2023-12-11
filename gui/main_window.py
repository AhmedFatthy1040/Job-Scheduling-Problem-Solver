import tkinter as tk
from tkinter import messagebox
from models.job import Job
from models.resource import Resource
from models.job_scheduling_problem import JobSchedulingProblem
from algorithms.backtracking_algorithm import BacktrackingAlgorithm
from algorithms.genetic_algorithm import GeneticAlgorithm

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Job Scheduling Problem Solver")

        self.jobs = []
        self.resources = []

        # Jobs Entry Fields
        self.job_id_label = tk.Label(root, text="Job ID:")
        self.job_id_label.grid(row=0, column=0)
        self.job_id_entry = tk.Entry(root)
        self.job_id_entry.grid(row=0, column=1)

        self.job_time_label = tk.Label(root, text="Job Time:")
        self.job_time_label.grid(row=1, column=0)
        self.job_time_entry = tk.Entry(root)
        self.job_time_entry.grid(row=1, column=1)

        self.dependency_label = tk.Label(root, text="Dependency:")
        self.dependency_label.grid(row=2, column=0)
        self.dependency_entry = tk.Entry(root)
        self.dependency_entry.grid(row=2, column=1)

        self.add_job_button = tk.Button(root, text="Add Job", command=self.add_job)
        self.add_job_button.grid(row=3, column=0, columnspan=2)

        # Resources Entry Fields
        self.resource_id_label = tk.Label(root, text="Resource ID:")
        self.resource_id_label.grid(row=4, column=0)
        self.resource_id_entry = tk.Entry(root)
        self.resource_id_entry.grid(row=4, column=1)

        self.capacity_label = tk.Label(root, text="Capacity:")
        self.capacity_label.grid(row=5, column=0)
        self.capacity_entry = tk.Entry(root)
        self.capacity_entry.grid(row=5, column=1)

        self.add_resource_button = tk.Button(root, text="Add Resource", command=self.add_resource)
        self.add_resource_button.grid(row=6, column=0, columnspan=2)

        # Solve Button
        self.solve_button = tk.Button(root, text="Solve", command=self.solve)
        self.solve_button.grid(row=7, column=0, columnspan=2)

    def add_job(self):
        job_id = int(self.job_id_entry.get())
        job_time = int(self.job_time_entry.get())
        dependency = self.dependency_entry.get()
        dependency = int(dependency) if dependency else None

        job = Job(job_id, job_time, dependency)
        self.jobs.append(job)

        messagebox.showinfo("Job Added", f"Job {job_id} added successfully!")

    def add_resource(self):
        resource_id = int(self.resource_id_entry.get())
        capacity = int(self.capacity_entry.get())

        resource = Resource(resource_id, capacity)
        self.resources.append(resource)

        messagebox.showinfo("Resource Added", f"Resource {resource_id} added successfully!")

    def solve(self):
        from gui.result_window import ResultWindow  # Import placed here to avoid circular import
        if self.jobs and self.resources:
            problem_instance = JobSchedulingProblem(self.jobs, self.resources)

            backtracking_algorithm = BacktrackingAlgorithm(problem_instance)
            genetic_algorithm = GeneticAlgorithm(problem_instance)

            result_root_backtracking = tk.Tk()
            result_window_backtracking = ResultWindow(result_root_backtracking, backtracking_algorithm, problem_instance)
            result_root_backtracking.mainloop()

            result_root_genetic = tk.Tk()
            result_window_genetic = ResultWindow(result_root_genetic, genetic_algorithm, problem_instance)
            result_root_genetic.mainloop()
        else:
            messagebox.showwarning("Incomplete Data", "Please add jobs and resources before solving.")