from integrators.scipy_ivp_integrator import integrate_system
from utils.body_converter import bodies_to_state_vector
from utils.body_data_loader import load_bodies_from_json
import numpy as np
import time

def main():
    # Load real DE440-based Body objects
    bodies = load_bodies_from_json(
        "data/body/positions.json",
        "data/body/velocities.json",
        "data/body/masses.json"
    )

    # Prepare flat initial state and masses
    y0 = bodies_to_state_vector(bodies)
    masses = np.array([body.mass for body in bodies])

    # Simulate for 3 years
    T = 1e2 * 365.25 * 24 * 3600
    t_eval = np.linspace(0, T, 100)

    print("Running integration...")
    start_time = time.perf_counter()  # Record start time
    solution = integrate_system(
        y0=y0,
        t_span=(0, T),
        masses=masses,
        t_eval=t_eval
    )

    # Execution process time
    end_time = time.perf_counter() # Record end time
    execution_time = end_time - start_time
    print("Integration complete!")
    print(f"Execution time: {execution_time:.2f} seconds")

if __name__ == "__main__":
    main()
