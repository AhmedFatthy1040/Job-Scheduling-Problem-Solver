class Resource:
    def __init__(self, resource_id, capacity):
        self.resource_id = resource_id
        self.capacity = capacity

    def __str__(self):
        return f"Resource {self.resource_id} (Capacity: {self.capacity})"