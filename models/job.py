from typing import Optional

class Job:
    """
    Represents a job in the scheduling problem.
    
    Attributes:
        job_id (int): Unique identifier for the job
        processing_time (int): Time required to complete the job
        dependency (Optional[int]): ID of job that must complete before this job can start
    """
    
    def __init__(self, job_id: int, processing_time: int, dependency: Optional[int] = None):
        """
        Initialize a Job instance.
        
        Args:
            job_id: Unique identifier for the job
            processing_time: Time required to complete the job (must be positive)
            dependency: ID of job that must complete before this job can start
            
        Raises:
            ValueError: If processing_time is not positive or if job_id equals dependency
        """
        if processing_time <= 0:
            raise ValueError("Processing time must be positive")
        if dependency is not None and dependency == job_id:
            raise ValueError("Job cannot depend on itself")
            
        self.job_id = job_id
        self.processing_time = processing_time
        self.dependency = dependency

    def __str__(self) -> str:
        """Return string representation of the job."""
        dependency_str = f"Job {self.dependency}" if self.dependency is not None else "None"
        return f"Job {self.job_id} (Processing Time: {self.processing_time}, Dependency: {dependency_str})"
    
    def __repr__(self) -> str:
        """Return detailed string representation for debugging."""
        return f"Job(job_id={self.job_id}, processing_time={self.processing_time}, dependency={self.dependency})"