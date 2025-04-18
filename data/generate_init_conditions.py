import spiceypy as spice
import numpy as np
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # base directory
KERNEL_DIR = os.path.join(BASE_DIR, "..", "kernels")  # go up to root then into kernels

# /kernels paths
BSP_PATH = os.path.join(KERNEL_DIR, "de440.bsp")
LSK_PATH = os.path.join(KERNEL_DIR, "naif0012.tls")
OUTPUT_DIR = os.path.join(BASE_DIR, "body")
EPOCH_UTC = "2025-01-01T00:00:00"
BODIES = {
    "Sun": "SUN",
    "Mercury": "MERCURY BARYCENTER",
    "Venus": "VENUS BARYCENTER",
    "Earth": "EARTH",
    "Mars": "MARS BARYCENTER",
    "Jupiter": "JUPITER BARYCENTER",
    "Saturn": "SATURN BARYCENTER",
    "Uranus": "URANUS BARYCENTER",
    "Neptune": "NEPTUNE BARYCENTER"
}

# Masses in kg from JPL
MASSES_KG = {
    "Sun": 1.9885e30,
    "Mercury": 3.3011e23,
    "Venus": 4.8675e24,
    "Earth": 5.9724e24,
    "Mars": 6.4171e23,
    "Jupiter": 1.8982e27,
    "Saturn": 5.6834e26,
    "Uranus": 8.6810e25,
    "Neptune": 1.0241e26
}

# Convert kilometer to meter
def km_to_m(arr):
    return (np.array(arr) * 1e3).tolist()

def main():
    # Load ephemeris
    spice.furnsh(LSK_PATH)
    spice.furnsh(BSP_PATH)
    et = spice.str2et(EPOCH_UTC)

    positions = {}
    velocities = {}
    masses = {}

    for name, spice_name in BODIES.items():
        state, _ = spice.spkezr(spice_name, et, "J2000", "NONE", "SOLAR SYSTEM BARYCENTER")
        positions[name] = km_to_m(state[:3])   # meters
        velocities[name] = km_to_m(state[3:6]) # m/s
        masses[name] = MASSES_KG[name]

    # Save to JSON files
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(os.path.join(OUTPUT_DIR, "positions.json"), "w") as f:
        json.dump(positions, f, indent=2)
    with open(os.path.join(OUTPUT_DIR, "velocities.json"), "w") as f:
        json.dump(velocities, f, indent=2)
    with open(os.path.join(OUTPUT_DIR, "masses.json"), "w") as f:
        json.dump(masses, f, indent=2)

    print("Initial planetary state saved to JSON files in /data/body/")


if __name__ == "__main__":
    main()