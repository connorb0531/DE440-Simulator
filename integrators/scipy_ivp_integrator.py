from scipy.integrate import solve_ivp
from dynamics.newtonian_gravity import n_body_ode

# Main integration function: solves the ODE system over time
def integrate_system(y0, t_span, masses, t_eval=None, method='RK45', rtol=1e-6, atol=1e-6):
    # Wrap the ODE system to match the format expected by solve_ivp
    def wrapped_ode(t, y):
        return n_body_ode(y, masses)

    # Solve the system of differential equations
    sol = solve_ivp(
        fun=wrapped_ode,    # the system to integrate
        t_span=t_span,      # start and end times
        y0=y0,              # initial state
        method=method,      # numerical integration method
        t_eval=t_eval,      # output time steps
        rtol=rtol,          # relative tolerance
        atol=atol           # absolute tolerance
    )

    return sol