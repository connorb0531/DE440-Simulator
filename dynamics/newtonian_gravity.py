import numpy as np
from data import constants

# Compute Newtonian gravitational acceleration
def compute_acceleration(r_i, r_j, M_j):
    diff_vector = r_j - r_i # Displacement vector
    magnitude = np.linalg.norm(diff_vector) # Magnitude of displacement vector

    if magnitude == 0: # Avoid division by 0 (If positions are identical, shouldn't happen)
        return np.zeros(3)

    return constants.G * M_j * diff_vector / magnitude ** 3 # Acceleration resultant

# Returns time derivative of system's state
def n_body_ode(t, bodies):
    # System body count
    N = len(bodies)

    # Extract current state into NumPy arrays
    positions = np.stack([body.position for body in bodies])    # shape: (N, 3)
    velocities = np.stack([body.velocity for body in bodies])   # shape: (N, 3)
    masses = np.stack([body.mass for body in bodies])           # shape: (N,)
    accelerations = np.zeros_like(positions)                    # shape: (N, 3)

    # Compute net acceleration on each body from all others
    for i in range(N):
        for j in range(N):
            if i != j:
                acc = compute_acceleration(positions[i], positions[j], masses[j])
                accelerations[i] += acc

    # Return flattened derivative vector:
    # First half = velocities, second half = accelerations
    derivatives = np.hstack((velocities, accelerations))    # shape: (N, 6)
    return derivatives.flatten()                            # shape: (6 * N,)