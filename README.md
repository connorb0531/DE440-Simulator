## Ephemeris Data (Required)

This project uses the official NASA JPL DE440 planetary ephemeris and leap seconds kernel.

To run the simulation, you must download the following files:

### DE440 Ephemeris (Planetary Positions & Velocities)

Download:
- [`de440.bsp`](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de440.bsp)

### Leap Seconds Kernel (Required for Time Conversions)

Download:
- [`naif0012.tls`](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/lsk/naif0012.tls)

### Place Both Files In: `/kernels/`


## Python Dependencies

Install required libraries:

```bash
pip install -r requirements.txt
```

## Getting Started
1. Run the initializer script to extract real planetary states:

```bash
python data/generate_init_conditions.py
```

