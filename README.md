## Ephemeris Data (Required)

This project uses the official NASA JPL DE440 planetary ephemeris.

To run the simulation, you must download the following files:

### DE440 Ephemeris (Planetary Positions & Velocities)

Download:
- [`de440.bsp`](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de440.bsp)


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

