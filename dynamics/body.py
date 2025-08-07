import numpy as np

# Represents celestial object
class Body:
    def __init__(self, name, mass, position, velocity):
        self.name = name
        self.mass = mass
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.zeros(3)
        self.history = None

    def __repr__(self):
        return f"{self.name}: mass={self.mass}, pos={self.position}, vel={self.velocity}"