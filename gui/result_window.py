import tkinter as tk
from tkinter import ttk

class ResultWindow:
    def __init__(self, master, algorithm, problem_instance):
        self.master = master
        self.algorithm = algorithm
        self.problem_instance = problem_instance
        
        self.master.title("Algorithm Results")
        self.master.geometry("700x600")
        
        self.setup_ui()
        self.display_results()
    
    def setup_ui(self):
        title = tk.Label(self.master, text="Scheduling Results", font=("Arial", 16, "bold"))
        title.pack(pady=10)
        
        algo_name = "Backtracking Algorithm" if hasattr(self.algorithm, 'backtrack') else "Genetic Algorithm"
        algo_label = tk.Label(self.master, text=f"Algorithm: {algo_name}", font=("Arial", 12))
        algo_label.pack(pady=5)
        
        text_frame = tk.Frame(self.master)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.result_text = tk.Text(text_frame, wrap=tk.WORD, font=("Courier", 10))
        scrollbar_y = ttk.Scrollbar(text_frame, orient="vertical", command=self.result_text.yview)
        scrollbar_x = ttk.Scrollbar(self.master, orient="horizontal", command=self.result_text.xview)
        
        self.result_text.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        
        close_button = tk.Button(self.master, text="Close", command=self.master.destroy, 
                               bg="#ff6b6b", fg="white", font=("Arial", 10, "bold"))
        close_button.pack(pady=10)

    def display_results(self):
        self.result_text.delete("1.0", tk.END)
        
        result_text = "PROBLEM INSTANCE:\n"
        result_text += "=" * 60 + "\n\n"
        
        result_text += "Jobs:\n"
        for job in self.problem_instance.jobs:
            dependency_str = f"Job {job.dependency}" if job.dependency else "None"
            result_text += f"  Job {job.job_id}: Processing Time = {job.processing_time}, Dependency = {dependency_str}\n"
        
        result_text += "\nResources:\n"
        for resource in self.problem_instance.resources:
            result_text += f"  Resource {resource.resource_id}: Capacity = {resource.capacity}\n"
        
        result_text += "\n" + "=" * 60 + "\n"
        result_text += "SOLUTION:\n"
        result_text += "=" * 60 + "\n\n"
        
        if self.algorithm:
            if hasattr(self.algorithm, 'evolve'):
                best_schedule = self.algorithm.best_schedule
            else:
                best_schedule = self.algorithm.best_schedule if self.algorithm.best_schedule else self.algorithm.solve()
            
            result_text += self.format_schedule(best_schedule)
        else:
            result_text += "No algorithm instance provided.\n"
        
        self.result_text.insert(tk.END, result_text)
        self.result_text.config(state=tk.DISABLED)
    
    def format_schedule(self, schedule):
        if schedule is None:
            return "No valid schedule found.\n"
        
        schedule_text = "Optimal Schedule:\n\n"
        
        resource_occupancy = {resource.resource_id: 0 for resource in self.problem_instance.resources}
        job_start_times = {job.job_id: 0 for job in self.problem_instance.jobs}
        
        total_makespan = 0
        
        for assignment in schedule:
            job = assignment[0]
            resource = assignment[1]
            
            dependency_start_time = 0
            if job.dependency is not None:
                dependency_start_time = job_start_times.get(job.dependency, 0)
            
            start_time = max(resource_occupancy[resource.resource_id], dependency_start_time)
            end_time = start_time + job.processing_time
            
            schedule_text += f"Job {job.job_id} → Resource {resource.resource_id}\n"
            schedule_text += f"  Start Time: {start_time}, End Time: {end_time}, Duration: {job.processing_time}\n"
            if job.dependency:
                schedule_text += f"  Dependency: Job {job.dependency}\n"
            schedule_text += "\n"
            
            resource_occupancy[resource.resource_id] = end_time
            job_start_times[job.job_id] = end_time
            total_makespan = max(total_makespan, end_time)
        
        schedule_text += f"PERFORMANCE METRICS:\n"
        schedule_text += f"Total Makespan: {total_makespan}\n\n"
        schedule_text += f"Resource Utilization:\n"
        for resource_id, end_time in resource_occupancy.items():
            resource = next(r for r in self.problem_instance.resources if r.resource_id == resource_id)
            utilization = (end_time / resource.capacity) * 100 if resource.capacity > 0 else 0
            schedule_text += f"  Resource {resource_id}: {end_time}/{resource.capacity} = {utilization:.1f}%\n"
        
        return schedule_text

if __name__ == "__main__":
    root = tk.Tk()
    app = ResultWindow(root, None, None)
    root.mainloop()