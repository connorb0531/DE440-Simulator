from scipy.integrate import solve_ivp
from dynamics.newtonian_gravity import n_body_ode, n_body_ode_vectorized

# Main integration function: solves the ODE system over time
def integrate_system(y0, t_span, masses, t_eval=None, method='RK45', rtol=1e-6, atol=1e-6, use_vectorized=False):
    """
    Integrate the N-body gravitational system.
    
    Parameters:
    -----------
    y0 : array_like
        Initial state vector
    t_span : tuple
        Integration time span (t_start, t_end)
    masses : array_like
        Masses of the bodies
    t_eval : array_like, optional
        Time points at which to evaluate the solution
    method : str, optional
        Integration method ('RK45', 'RK23', etc.)
    rtol : float, optional
        Relative tolerance
    atol : float, optional
        Absolute tolerance
    use_vectorized : bool, optional
        If True, use vectorized NumPy implementation instead of loop-based Numba version
    """
    # Choose which ODE function to use
    ode_function = n_body_ode_vectorized if use_vectorized else n_body_ode
    
    # Wrap the ODE system to match the format expected by solve_ivp
    def wrapped_ode(t, y):
        return ode_function(y, masses)

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