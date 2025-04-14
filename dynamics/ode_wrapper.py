# dynamics/ode_wrapper.py
from utils.body_converter import state_vector_to_bodies
from dynamics.newtonian_gravity import n_body_ode

def ode_wrapper(t, y, masses):
    bodies = state_vector_to_bodies(y, masses)
    return n_body_ode(t, bodies)
