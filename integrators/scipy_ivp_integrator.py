from scipy.integrate import solve_ivp
import numpy as np

def integrate_system(ode_func, y0, t_span, masses, t_eval=None, method='RK45', rtol=1e-9, atol=1e-9):

    # Wrap the ODE function to pass masses into it
    def wrapped_ode(t, y):
        return ode_func(t, y, masses)

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