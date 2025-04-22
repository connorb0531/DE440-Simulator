import numpy as np
from data import constants
from numba import njit

# Compute Newtonian gravitational acceleration
@njit()
def compute_acceleration(r_i, r_j, M_j):
    diff_vector = r_j - r_i # Displacement vector
    magnitude = np.linalg.norm(diff_vector) # Magnitude of displacement vector

    if magnitude == 0: # Avoid division by 0 (If positions are identical, shouldn't happen)
        return np.zeros(3)

    return constants.G * M_j * diff_vector / magnitude ** 3 # Acceleration resultant

# Returns time derivative of system's state
@njit()
def n_body_ode(y, masses):
    # System body count
    N = len(masses)

    # Extract current bodies' state into NumPy arrays
    y = y.reshape((N, 6))
    positions = y[:, :3]
    velocities = y[:, 3:]
    accelerations = np.zeros_like(positions)

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