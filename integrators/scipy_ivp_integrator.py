from scipy.integrate import solve_ivp
from dynamics.newtonian_gravity import n_body_ode
from utils.body_converter import state_vector_to_bodies

def ode_wrapper(t, y, masses):
    bodies = state_vector_to_bodies(y, masses)
    return n_body_ode(t, bodies)

def integrate_system(y0, t_span, masses, t_eval=None, method='RK45', rtol=1e-6, atol=1e-6):
    def wrapped_ode(t, y):
        return ode_wrapper(t, y, masses)

    sol = solve_ivp(
        fun=wrapped_ode,
        t_span=t_span,
        y0=y0,
        method=method,
        t_eval=t_eval,
        rtol=rtol,
        atol=atol
    )
    return sol