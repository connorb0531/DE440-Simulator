from integrators.scipy_ivp_integrator import integrate_system
from utils.body_converter import bodies_to_state_vector
from utils.body_data_loader import load_bodies_from_json
import numpy as np

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

    # Simulate for 10,000 days
    T = 1e4 * 24 * 3600
    t_eval = np.linspace(0, T, 100)

    print("Running integration...")
    solution = integrate_system(
        y0=y0,
        t_span=(0, T),
        masses=masses,
        t_eval=t_eval
    )

    # Debug info
    print("Integration complete!")
    print("Final time reached:", solution.t[-1])
    print("State shape:", solution.y.shape)

if __name__ == "__main__":
    main()
