class JobSchedulingProblem:
    def __init__(self, jobs, resources):
        self.jobs = jobs
        self.resources = resources

    def display_problem(self):
        print("Jobs:")
        for job in self.jobs:
            print(f"Job {job.job_id} (Processing Time: {job.processing_time}, Dependencies: {job.dependencies})")

        print("\nResources:")
        for resource in self.resources:
            print(f"Resource {resource.resource_id} (Capacity: {resource.capacity})")