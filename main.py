from models.resource import Resource
from models.job import Job
from models.job_scheduling_problem import JobSchedulingProblem

jobs = [
    Job(1, 3),
    Job(2, 5, 1),
    Job(3, 2, 2),
]

resources = [
    Resource(1, 6),
    Resource(2, 4),
]

jsp = JobSchedulingProblem(jobs, resources)

jsp.display_problem()