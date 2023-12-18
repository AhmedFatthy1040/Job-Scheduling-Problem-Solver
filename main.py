import tkinter as tk
from tkinter import messagebox
from gui.main_window import MainWindow

root = tk.Tk()
app = MainWindow(root)
root.mainloop()

# ------------------------------------------

# from models.resource import Resource
# from models.job import Job
# from models.job_scheduling_problem import JobSchedulingProblem
# from algorithms.backtracking_algorithm import BacktrackingAlgorithm
# from algorithms.genetic_algorithm import GeneticAlgorithm
# from utils.random_generator import RandomGenerator
# from utils.scheduler_evaluator import SchedulerEvaluator

# instances = []
# for instance_id in range(1, 6):
#     jobs = [RandomGenerator.generate_random_job(job_id) for job_id in range(1, 6)]
#     resources = [RandomGenerator.generate_random_resource(resource_id) for resource_id in range(1, 4)]

#     problem_instance = JobSchedulingProblem(jobs, resources)
#     instances.append(problem_instance)

# total_backtracking = 0
# total_genetic = 0

# for instance in instances:
#     evaluator = SchedulerEvaluator(instance)
#     evaluator.run_algorithms()
#     comparison_results, avg_backtracking_time, avg_genetic_time = evaluator.evaluate_performance()

#     for result in comparison_results:
#         if result == 0:
#             print("Backtracking Algorithm is faster.")
#             total_backtracking += 1
#         elif result == 1:
#             print("Genetic Algorithm is faster.")
#             total_genetic += 1
#         elif result == 2:
#             print("Both algorithms made the same schedule.")

#     print(f"Avg Backtracking Time: {avg_backtracking_time} seconds")
#     print(f"Avg Genetic Time: {avg_genetic_time} seconds")

# if total_backtracking > total_genetic:
#     print("On average, Backtracking Algorithm is faster.")
# elif total_backtracking < total_genetic:
#     print("On average, Genetic Algorithm is faster.")
# else:
#     print("On average, both algorithms have the same performance.")