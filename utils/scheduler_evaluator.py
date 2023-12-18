import time
from algorithms.backtracking_algorithm import BacktrackingAlgorithm
from algorithms.genetic_algorithm import GeneticAlgorithm

class SchedulerEvaluator:
    def __init__(self, instance):
        self.instance = instance
        self.backtracking_results = []
        self.genetic_results = []
        self.problem_instance = instance

    def run_algorithms(self):
        # Run Backtracking Algorithm
        backtracking_algorithm = BacktrackingAlgorithm(self.instance)
        start_time_backtracking = time.time()
        backtracking_algorithm.solve()
        end_time_backtracking = time.time()
        duration_backtracking = end_time_backtracking - start_time_backtracking
        backtracking_schedule = backtracking_algorithm.best_schedule
        self.backtracking_results.append((backtracking_schedule, duration_backtracking))

        # Run Genetic Algorithm
        genetic_algorithm = GeneticAlgorithm(self.instance)
        start_time_genetic = time.time()
        genetic_algorithm.initialize_population()
        genetic_algorithm.evolve()
        end_time_genetic = time.time()
        duration_genetic = end_time_genetic - start_time_genetic
        genetic_schedule = genetic_algorithm.best_schedule
        self.genetic_results.append((genetic_schedule, duration_genetic))
    
    def get_schedule_representation(self, schedule):
        schedule_representation = ""
        resource_occupancy = {resource.resource_id: 0 for resource in self.problem_instance.resources}
        job_start_times = {job.job_id: 0 for job in self.problem_instance.jobs}

        valid_schedule = True  # Flag to track the validity of the schedule

        for assignment in schedule:
            job = assignment[0]
            resource = assignment[1]

            dependency_start_time = job_start_times[job.dependency] if job.dependency is not None else 0
            start_time = max(resource_occupancy[resource.resource_id], dependency_start_time)
            end_time = start_time + job.processing_time

            # Check if the assignment makes the schedule invalid
            if resource_occupancy[resource.resource_id] + job.processing_time > resource.capacity \
                    or (job.dependency is not None and job_start_times[job.dependency] > start_time):
                valid_schedule = False
                break

            schedule_representation += (
                f"Job {job.job_id} scheduled on Resource {resource.resource_id} "
                f"Start Time: {start_time}, End Time: {end_time}\n"
            )

            resource_occupancy[resource.resource_id] = end_time
            job_start_times[job.job_id] = end_time

        if not valid_schedule:
            schedule_representation = "No valid schedule found."

        return schedule_representation

    def extract_total_time_span(self, schedule_str):
        lines = schedule_str.split("\n")

        # Extract end times from each line and find the maximum
        end_times = [int(line.split("End Time: ")[1]) for line in lines if "End Time" in line]

        if not end_times:
            # No valid schedule found, return a default value or indication
            return "No valid schedule found."

        total_time_span = max(end_times)
        return total_time_span

    def evaluate_performance(self):
        comparison_results = []
        backtracking_times = []
        genetic_times = []

        for i, (backtracking_schedule, duration_backtracking) in enumerate(self.backtracking_results):
            genetic_schedule, duration_genetic = self.genetic_results[i]

            if backtracking_schedule is None and genetic_schedule is not None:
                comparison_results.append(1)  # Genetic is faster or valid when backtracking isn't
            elif backtracking_schedule is not None and genetic_schedule is None:
                comparison_results.append(0)  # Backtracking is faster or valid when genetic isn't
            elif backtracking_schedule is None and genetic_schedule is None:
                comparison_results.append(2)  # Both schedules are invalid
            else:
                # Get Schedule Representations
                schedule_representation_backtracking = self.get_schedule_representation(backtracking_schedule)
                schedule_representation_genetic = self.get_schedule_representation(genetic_schedule)

                # Calculate Total Time Span
                total_time_span_backtracking = self.extract_total_time_span(schedule_representation_backtracking)
                total_time_span_genetic = self.extract_total_time_span(schedule_representation_genetic)

                if total_time_span_backtracking == "No valid schedule found." and total_time_span_genetic != "No valid schedule found.":
                    comparison_results.append(1)  # Genetic is faster or valid when backtracking isn't
                elif total_time_span_backtracking != "No valid schedule found." and total_time_span_genetic == "No valid schedule found.":
                    comparison_results.append(0)  # Backtracking is faster or valid when genetic isn't
                elif total_time_span_backtracking < total_time_span_genetic:
                    comparison_results.append(0)
                elif total_time_span_backtracking > total_time_span_genetic:
                    comparison_results.append(1)
                else:
                    comparison_results.append(2)

            # Record Algorithm Times
            backtracking_times.append(duration_backtracking)
            genetic_times.append(duration_genetic)

        # Calculate Average Times
        avg_backtracking_time = sum(backtracking_times) / len(backtracking_times)
        avg_genetic_time = sum(genetic_times) / len(genetic_times)

        return comparison_results, avg_backtracking_time, avg_genetic_time
