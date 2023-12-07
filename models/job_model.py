class Job:
    def __init__(self, job_id, processing_time, dependencies=None):
        self.job_id = job_id
        self.processing_time = processing_time
        self.dependencies = dependencies if dependencies is not None else []

    def __str__(self):
        return f"Job {self.job_id} (Processing Time: {self.processing_time}, Dependencies: {self.dependencies})"