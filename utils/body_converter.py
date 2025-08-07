import numpy as np

# Converts bodies class into state NumpPy array
def bodies_to_state_vector(bodies):
    positions = np.array([body.position for body in bodies])
    velocities = np.array([body.velocity for body in bodies])
    return np.hstack((positions, velocities)).flatten()