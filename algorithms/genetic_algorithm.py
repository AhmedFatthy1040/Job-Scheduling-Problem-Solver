import random

class GeneticAlgorithm:
    def __init__(self, problem_instance, population_size=50, generations=100, crossover_prob=0.8, mutation_prob=0.2):
        self.problem_instance = problem_instance
        self.population_size = population_size
        self.generations = generations
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob
        self.population = []
        self.best_schedule = None

    def initialize_population(self):
        for _ in range(self.population_size):
            schedule = self.generate_random_schedule()
            self.population.append(schedule)

    def generate_random_schedule(self):
        schedule = []
        jobs = self.problem_instance.jobs.copy()

        for job in jobs:
            resource = random.choice(self.problem_instance.resources)
            schedule.append((job, resource))

        return schedule

    def fitness(self, schedule):
        if not self.is_valid_schedule(schedule):
            return float('inf')

        makespan = self.calculate_makespan(schedule)
        return makespan

    def is_valid_schedule(self, schedule):
        resource_occupancy = {resource.resource_id: 0 for resource in self.problem_instance.resources}

        for job, resource in schedule:
            if resource_occupancy[resource.resource_id] + job.processing_time > resource.capacity:
                return False

            if job.dependency is not None:
                dependency_scheduled = False
                for j, _ in schedule:
                    if j.job_id == job.dependency:
                        dependency_scheduled = True
                        break
                if not dependency_scheduled:
                    return False

            resource_occupancy[resource.resource_id] += job.processing_time

        return True

    def calculate_makespan(self, schedule):
        resource_occupancy = {resource.resource_id: 0 for resource in self.problem_instance.resources}

        for job, resource in schedule:
            dependency_start_time = 0 if job.dependency is None else self.get_job_end_time(job.dependency, schedule, resource_occupancy)
            start_time = max(resource_occupancy[resource.resource_id], dependency_start_time)
            end_time = start_time + job.processing_time

            resource_occupancy[resource.resource_id] = end_time

        return max(resource_occupancy.values())

    def get_job_end_time(self, job_id, schedule, resource_occupancy):
        for job, resource in schedule:
            if job.job_id == job_id:
                dependency_start_time = 0 if job.dependency is None else self.get_job_end_time(job.dependency, schedule, resource_occupancy)
                start_time = max(resource_occupancy.get(resource.resource_id, 0), dependency_start_time)
                return start_time + job.processing_time
        return 0

    def crossover(self, parent1, parent2):
        if len(parent1) > 1:
            crossover_point = random.randint(1, len(parent1) - 1)
        else:
            crossover_point = 1
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    def mutate(self, schedule):
        mutated_schedule = schedule.copy()
        job_index = random.randint(0, len(mutated_schedule) - 1)
        new_resource = random.choice(self.problem_instance.resources)
        mutated_schedule[job_index] = (mutated_schedule[job_index][0], new_resource)
        return mutated_schedule

    def select_parents(self):
        sorted_population = sorted(self.population, key=lambda x: self.fitness(x))
        return sorted_population[:int(self.population_size * 0.2)]

    def evolve(self):
        self.initialize_population()

        for generation in range(self.generations):
            parents = self.select_parents()
            offspring = []

            while len(offspring) < self.population_size - len(parents):
                parent1, parent2 = random.sample(parents, 2)

                if random.random() < self.crossover_prob:
                    child1, child2 = self.crossover(parent1, parent2)
                else:
                    child1, child2 = parent1, parent2

                if random.random() < self.mutation_prob:
                    child1 = self.mutate(child1)

                if random.random() < self.mutation_prob:
                    child2 = self.mutate(child2)

                offspring.extend([child1, child2])

            self.population = parents + offspring

            current_best_schedule = min(self.population, key=lambda x: self.fitness(x))

            if self.best_schedule is None or self.fitness(current_best_schedule) < self.fitness(self.best_schedule):
                self.best_schedule = current_best_schedule

        self.display_schedule(self.best_schedule)
        return self.best_schedule

    def display_schedule(self, schedule):
        print("Optimal Schedule (Genetic Algorithm):")
        resource_occupancy = {resource.resource_id: 0 for resource in self.problem_instance.resources}
        job_start_times = {job.job_id: 0 for job in self.problem_instance.jobs}
        
        for assignment in schedule:
            job = assignment[0]
            resource = assignment[1]

            dependency_start_time = job_start_times[job.dependency] if job.dependency is not None else 0
            start_time = max(resource_occupancy[resource.resource_id], dependency_start_time)
            end_time = start_time + job.processing_time

            print(f"Job {job.job_id} scheduled on Resource {resource.resource_id} "
                f"Start Time: {start_time}, End Time: {end_time}")

            resource_occupancy[resource.resource_id] = end_time
            job_start_times[job.job_id] = end_time