class BacktrackingAlgorithm:
    def __init__(self, problem_instance):
        self.problem_instance = problem_instance
        self.best_schedule = None

    def is_valid_schedule(self, schedule):
        resource_occupancy = {resource.resource_id: 0 for resource in self.problem_instance.resources}

        for job, resource in schedule:
            # Check Resource Capacity
            if resource_occupancy[resource.resource_id] + job.processing_time > resource.capacity:
                return False

            # Check job dependencies
            if job.dependency is not None and job.dependency not in [j.job_id for j, _ in schedule]:
                return False

            # Update Resource Occupancy
            resource_occupancy[resource.resource_id] += job.processing_time

        return True

    def backtrack(self, schedule, remaining_jobs):
        if not remaining_jobs:
            if self.is_valid_schedule(schedule):
                if self.best_schedule is None or len(schedule) < len(self.best_schedule):
                    self.best_schedule = schedule.copy()
            return

        current_job = remaining_jobs[0]

        for resource in self.problem_instance.resources:
            new_schedule = schedule.copy()
            new_schedule.append((current_job, resource))

            new_remaining_jobs = remaining_jobs[1:]
            self.backtrack(new_schedule, new_remaining_jobs)

    def solve(self):
        initial_schedule = []
        remaining_jobs = self.problem_instance.jobs.copy()

        self.backtrack(initial_schedule, remaining_jobs)

        if self.best_schedule:
            self.display_schedule()
        else:
            print("No valid schedule found.")

    def display_schedule(self):
        print("Optimal Schedule:")
        resource_occupancy = {resource.resource_id: 0 for resource in self.problem_instance.resources}

        for assignment in self.best_schedule:
            job = assignment[0]
            resource = assignment[1]
            start_time = resource_occupancy[resource.resource_id]
            end_time = start_time + job.processing_time

            print(f"Job {job.job_id} scheduled on Resource {resource.resource_id} "
                f"Start Time: {start_time}, End Time: {end_time}")

            # Update Resource Occupancy
            resource_occupancy[resource.resource_id] = end_time
