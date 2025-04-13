import json
from dynamics.body import Body

def load_bodies_from_json(pos_path, vel_path, mass_path):
    with open(pos_path) as f:
        positions = json.load(f)
    with open(vel_path) as f:
        velocities = json.load(f)
    with open(mass_path) as f:
        masses = json.load(f)

    bodies = []
    for name in positions:
        body = Body(
            name=name,
            mass=masses[name],
            position=positions[name],
            velocity=velocities[name]
        )
        bodies.append(body)

    return bodies
