import numpy as np
from dynamics.body import Body

def bodies_to_state_vector(bodies):
    positions = np.array([body.position for body in bodies])
    velocities = np.array([body.velocity for body in bodies])
    return np.hstack((positions, velocities)).flatten()

def state_vector_to_bodies(y, masses):
    N = len(masses)
    y = y.reshape(N, 6)

    bodies = []
    for i in range(N):
        position = y[i, :3]
        velocity = y[i, 3:]
        body = Body(
            name=f"Body_{i}",
            mass=masses[i],
            position=position,
            velocity=velocity
        )
        bodies.append(body)

    return bodies