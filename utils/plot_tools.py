import matplotlib.pyplot as plt
import numpy as np

def plot_orbits_3d(bodies):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Set entire figure and axes background to black
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    # Hide panes (background walls)
    ax.xaxis.pane.set_visible(False)
    ax.yaxis.pane.set_visible(False)
    ax.zaxis.pane.set_visible(False)

    # Hide grid and ticks
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    # Hide axis lines
    ax.xaxis.line.set_color((0.0, 0.0, 0.0, 0.0))
    ax.yaxis.line.set_color((0.0, 0.0, 0.0, 0.0))
    ax.zaxis.line.set_color((0.0, 0.0, 0.0, 0.0))

    # Plot each body's trajectory
    for body in bodies:
        if body.history is None:
            continue
        pos = np.array(body.history)
        ax.plot(pos[:, 0], pos[:, 1], pos[:, 2], label=body.name)

    ax.legend(labelcolor='white', loc='upper left')

    plt.show()
