class Resource:
    """
    Represents a resource in the scheduling problem.
    
    Attributes:
        resource_id (int): Unique identifier for the resource
        capacity (int): Maximum total processing time this resource can handle
    """
    
    def __init__(self, resource_id: int, capacity: int):
        """
        Initialize a Resource instance.
        
        Args:
            resource_id: Unique identifier for the resource
            capacity: Maximum total processing time this resource can handle (must be positive)
            
        Raises:
            ValueError: If capacity is not positive
        """
        if capacity <= 0:
            raise ValueError("Resource capacity must be positive")
            
        self.resource_id = resource_id
        self.capacity = capacity

    def __str__(self) -> str:
        """Return string representation of the resource."""
        return f"Resource {self.resource_id} (Capacity: {self.capacity})"
    
    def __repr__(self) -> str:
        """Return detailed string representation for debugging."""
        return f"Resource(resource_id={self.resource_id}, capacity={self.capacity})"