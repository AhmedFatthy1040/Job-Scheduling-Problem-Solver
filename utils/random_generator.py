import random
from models.resource import Resource
from models.job import Job

class RandomGenerator:
    @staticmethod
    def generate_random_job(job_id):
        processing_time = random.randint(1, 10)
        dependency = random.choice([None, job_id - 1]) if job_id > 1 else None
        return Job(job_id, processing_time, dependency)

    @staticmethod
    def generate_random_resource(resource_id):
        capacity = random.randint(3, 20)
        return Resource(resource_id, capacity)
