import data.generate_init_conditions
from utils.body_data_loader import load_bodies_from_json

bodies = load_bodies_from_json(
    "data/body/positions.json",
    "data/body/velocities.json",
    "data/body/masses.json"
)

print(bodies)