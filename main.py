from models.resource import Resource
from models.job import Job
from models.job_scheduling_problem import JobSchedulingProblem
from algorithms.backtracking_algorithm import BacktrackingAlgorithm

# Define the job scheduling problem instance
jobs = [
    Job(1, 3),
    Job(2, 1, dependency=1),
    Job(3, 4),
]

resources = [
    Resource(1, 6),
    Resource(2, 4),
]

jsp = JobSchedulingProblem(jobs, resources)

# Create an instance of the BacktrackingAlgorithm and solve the problem
backtracking_algorithm = BacktrackingAlgorithm(jsp)
backtracking_algorithm.solve()
