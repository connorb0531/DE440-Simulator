import numpy as np
from integrators.scipy_ivp_integrator import integrate_system
from utils.body_converter import bodies_to_state_vector
from utils.body_data_loader import load_bodies_from_json

def run_simulation(T, steps=100, file='ipynb'):
    positions_path = 'data/body/positions.json'
    velocities_path = 'data/body/velocities.json'
    masses_path = 'data/body/masses.json'

    if file == 'ipynb':
        positions_path = '../' + positions_path
        velocities_path = '../' + velocities_path
        masses_path =  '../' + masses_path
    if file == 'py':
        pass

    # Load body classes from json data
    bodies = load_bodies_from_json(positions_path, velocities_path, masses_path)

    # Convert to flat arrays
    y0 = bodies_to_state_vector(bodies)
    masses = np.array([body.mass for body in bodies])
    t_eval = np.linspace(0, T, steps)

    # Integrate
    solution = integrate_system(y0=y0, t_span=(0, T), masses=masses, t_eval=t_eval)

    # Attach position history
    state_trajectories = solution.y.T
    for i, body in enumerate(bodies):
        body.history = state_trajectories[:, i * 6 : i * 6 + 3]

    return bodies, solution