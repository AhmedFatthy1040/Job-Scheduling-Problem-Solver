import tkinter as tk

class ResultWindow:
    def __init__(self, master, algorithm, problem_instance):
        self.master = master
        self.algorithm = algorithm
        self.problem_instance = problem_instance

        self.result_text = tk.Text(master, wrap=tk.WORD, height=20, width=60)
        self.result_text.grid(row=0, column=0, padx=10, pady=10)

        self.display_results()

    def display_results(self):
        if self.algorithm:
            if hasattr(self.algorithm, 'evolve'):
                self.algorithm.initialize_population()
                best_schedule = self.algorithm.evolve()
            else:
                best_schedule = self.algorithm.solve()

            self.display_schedule(best_schedule)
        else:
            self.result_text.insert(tk.END, "No algorithm instance provided.")

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

if __name__ == "__main__":
    # Example usage
    root = tk.Tk()
    app = ResultWindow(root, None, None)  # Replace with actual algorithm and problem_instance
    root.mainloop()