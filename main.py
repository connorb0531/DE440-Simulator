import numpy as np
from utils.body_data_loader import load_bodies_from_json
from utils.body_converter import bodies_to_state_vector
from integrators.scipy_ivp_integrator import integrate_system
from dynamics.ode_wrapper import ode_wrapper

# Load real DE440-based Body objects
bodies = load_bodies_from_json(
    "data/body/positions.json",
    "data/body/velocities.json",
    "data/body/masses.json"
)

# Prepare flat initial state and masses
y0 = bodies_to_state_vector(bodies)
masses = np.array([body.mass for body in bodies])

# Simulate 1 year
T = 365.25 * 24 * 3600
t_eval = np.linspace(0, T, 5)

# Integrate using SciPy
solution = integrate_system(
    ode_func=ode_wrapper,
    y0=y0,
    t_span=(0, T),
    masses=masses,
    t_eval=t_eval
)

print("Integration successful:", solution.success)
print("Final time reached:", solution.t[-1])
print("Shape of solution.y:", solution.y.shape)
