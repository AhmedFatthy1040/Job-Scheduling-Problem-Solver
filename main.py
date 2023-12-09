from models.resource import Resource
from models.job import Job
from models.job_scheduling_problem import JobSchedulingProblem
from algorithms.backtracking_algorithm import BacktrackingAlgorithm

# Define the job scheduling problem instance
jobs = [
    Job(1, 3),
    Job(2, 1, dependency=1),
    Job(3, 4),
    Job(4, 5, dependency=3),
    Job(5, 1, dependency=3),
]

resources = [
    Resource(1, 6),
    Resource(2, 4),
    Resource(3, 5),
]

problem_instance = JobSchedulingProblem(jobs, resources)

# Create an instance of the BacktrackingAlgorithm and solve the problem
backtracking_algorithm = BacktrackingAlgorithm(problem_instance)
backtracking_algorithm.solve()
