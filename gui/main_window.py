import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from gui.algorithms_comparison_window import AlgorithmComparisonWindow
from gui.result_window import ResultWindow
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

        self.job_time_label = tk.Label(root, text="Job Time:")
        self.job_time_label.grid(row=0, column=0)
        self.job_time_entry = tk.Entry(root)
        self.job_time_entry.grid(row=0, column=1)

        self.dependency_label = tk.Label(root, text="Dependency:")
        self.dependency_label.grid(row=0, column=2)
        self.dependency_entry = tk.Entry(root)
        self.dependency_entry.grid(row=0, column=3)

        self.add_job_button = tk.Button(root, text="Add Job", command=self.add_job)
        self.add_job_button.grid(row=0, column=4)

        self.capacity_label = tk.Label(root, text="Capacity:")
        self.capacity_label.grid(row=1, column=0)
        self.capacity_entry = tk.Entry(root)
        self.capacity_entry.grid(row=1, column=1)

        self.add_resource_button = tk.Button(root, text="Add Resource", command=self.add_resource)
        self.add_resource_button.grid(row=1, column=2)

        self.jobs_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.jobs_listbox.grid(row=2, column=0, columnspan=3, rowspan=2, padx=5, pady=5, sticky="nsew")
        jobs_scrollbar_y = tk.Scrollbar(root, command=self.jobs_listbox.yview)
        jobs_scrollbar_y.grid(row=2, column=3, rowspan=2, sticky="nse")
        jobs_scrollbar_x = tk.Scrollbar(root, command=self.jobs_listbox.xview, orient=tk.HORIZONTAL)
        jobs_scrollbar_x.grid(row=4, column=0, columnspan=3, sticky="ew")
        self.jobs_listbox.config(yscrollcommand=jobs_scrollbar_y.set, xscrollcommand=jobs_scrollbar_x.set)

        self.resources_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.resources_listbox.grid(row=2, column=3, columnspan=2, rowspan=2, padx=5, pady=5, sticky="nsew")
        resources_scrollbar_y = tk.Scrollbar(root, command=self.resources_listbox.yview)
        resources_scrollbar_y.grid(row=2, column=5, rowspan=2, sticky="nse")
        resources_scrollbar_x = tk.Scrollbar(root, command=self.resources_listbox.xview, orient=tk.HORIZONTAL)
        resources_scrollbar_x.grid(row=4, column=3, columnspan=2, sticky="ew")
        self.resources_listbox.config(yscrollcommand=resources_scrollbar_y.set, xscrollcommand=resources_scrollbar_x.set)

        self.solve_backtracking_button = tk.Button(root, text="Solve with Backtracking", command=self.solve_backtracking)
        self.solve_backtracking_button.grid(row=4, column=0, columnspan=2, pady=5)

        self.solve_genetic_button = tk.Button(root, text="Solve with Genetic", command=self.solve_genetic)
        self.solve_genetic_button.grid(row=4, column=2, columnspan=2, pady=5)

        self.clear_jobs_button = tk.Button(root, text="Clear Jobs List", command=self.clear_jobs_list)
        self.clear_jobs_button.grid(row=6, column=0, columnspan=2, pady=5)

        self.clear_resources_button = tk.Button(root, text="Clear Resources List", command=self.clear_resources_list)
        self.clear_resources_button.grid(row=6, column=2, columnspan=2, pady=5)

        self.algorithm_comparison_button = tk.Button(root, text="Algorithm Comparison", command=self.open_algorithm_comparison)
        self.algorithm_comparison_button.grid(row=6, column=4, pady=5)

        self.job_id_counter = 1
        self.resource_id_counter = 1

    def add_job(self):
        try:
            job_time_text = self.job_time_entry.get().strip()
            if not job_time_text:
                messagebox.showerror("Invalid Input", "Please enter a job processing time.")
                return
            
            job_time = int(job_time_text)
            if job_time <= 0:
                messagebox.showerror("Invalid Input", "Job processing time must be positive.")
                return
            
            dependency_text = self.dependency_entry.get().strip()
            dependency = None
            if dependency_text:
                dependency = int(dependency_text)
                if dependency <= 0 or dependency >= self.job_id_counter:
                    messagebox.showerror("Invalid Input", f"Dependency must be between 1 and {self.job_id_counter - 1}.")
                    return

            job = Job(self.job_id_counter, job_time, dependency)
            self.jobs.append(job)
            self.jobs_listbox.insert(tk.END, f"Job {self.job_id_counter}: Time={job_time}, Dependency={dependency}")
            self.job_id_counter += 1

            self.job_time_entry.delete(0, tk.END)
            self.dependency_entry.delete(0, tk.END)

            messagebox.showinfo("Job Added", f"Job {job.job_id} added successfully!")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

    def add_resource(self):
        try:
            capacity_text = self.capacity_entry.get().strip()
            if not capacity_text:
                messagebox.showerror("Invalid Input", "Please enter a resource capacity.")
                return
            
            capacity = int(capacity_text)
            if capacity <= 0:
                messagebox.showerror("Invalid Input", "Resource capacity must be positive.")
                return

            resource = Resource(self.resource_id_counter, capacity)
            self.resources.append(resource)
            self.resources_listbox.insert(tk.END, f"Resource {self.resource_id_counter}: Capacity={capacity}")
            self.resource_id_counter += 1

            self.capacity_entry.delete(0, tk.END)

            messagebox.showinfo("Resource Added", f"Resource {resource.resource_id} added successfully!")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric value for capacity.")

    def solve_backtracking(self):
        self.solve(BacktrackingAlgorithm)

    def solve_genetic(self):
        self.solve(GeneticAlgorithm)

    def solve(self, algorithm_class):
        if self.jobs and self.resources:
            problem_instance = JobSchedulingProblem(self.jobs, self.resources)
            algorithm = algorithm_class(problem_instance)

            if algorithm_class == GeneticAlgorithm:
                algorithm.initialize_population()
                algorithm.evolve()
            else:
                algorithm.solve()

            result_root = tk.Tk()
            result_window = ResultWindow(result_root, algorithm, problem_instance)
            result_root.mainloop()
        else:
            messagebox.showwarning("Incomplete Data", "Please add jobs and resources before solving.")

    def clear_jobs_list(self):
        self.jobs_listbox.delete(0, tk.END)
        self.jobs = []
        self.job_id_counter = 1

    def clear_resources_list(self):
        self.resources_listbox.delete(0, tk.END)
        self.resources = []
        self.resource_id_counter = 1

    def open_algorithm_comparison(self):
        comparison_root = tk.Tk()
        comparison_window = AlgorithmComparisonWindow(comparison_root)
        comparison_root.mainloop()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
