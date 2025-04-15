import numpy as np
from data import constants

# Point-mass acceleration interaction between bodies
def compute_acceleration(r_i, r_j, M_j):
    diff_vector = r_j - r_i # Displacement vector
    magnitude = np.linalg.norm(diff_vector) # Magnitude of displacement vector

    if magnitude == 0: # Avoid division by 0 (unlikely case)
        return np.zeros(3)

    return constants.G * M_j * diff_vector / magnitude ** 3 # Acceleration resultant

# Returns derivative of system's state
def n_body_ode(t, bodies):
    # System body count
    N = len(bodies)

    # System's state of bodies
    positions = np.stack([body.position for body in bodies])
    velocities = np.stack([body.velocity for body in bodies])
    masses = np.stack([body.mass for body in bodies])
    accelerations = np.zeros_like(positions)

    for i in range(N):
        for j in range(N):
            if i != j:
                acc = compute_acceleration(positions[i], positions[j], masses[j])
                accelerations[i] += acc


    derivatives = np.hstack((velocities, accelerations))
    return derivatives.flatten()