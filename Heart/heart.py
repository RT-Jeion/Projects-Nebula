import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create figure
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor('black')

# Time variable
t = np.linspace(0, 2*np.pi, 1000)

# Create line objects (glow + main)
glow_line, = ax.plot([], [], linewidth=8, alpha=0.2)
main_line, = ax.plot([], [], linewidth=2)

# Text
text = ax.text(0, 0, "❤️", fontsize=20, ha='center', va='center')

# Animation function
def animate(frame):
    # Heartbeat scale
    scale = 1 + 0.1 * np.sin(frame * 0.2)

    # Heart equations
    x = scale * (16 * np.sin(t)**3)
    y = scale * (13 * np.cos(t)
                 - 5 * np.cos(2*t)
                 - 2 * np.cos(3*t)
                 - np.cos(4*t))

    # Color animation
    color = plt.cm.plasma((np.sin(frame * 0.1) + 1) / 2)

    # Update lines
    glow_line.set_data(x, y)
    glow_line.set_color(color)

    main_line.set_data(x, y)
    main_line.set_color(color)

    # Animate text (pulse)
    text.set_fontsize(20 + 10 * np.sin(frame * 0.2))
    text.set_position((0, 0))

    return glow_line, main_line, text

# Create animation
ani = FuncAnimation(fig, animate, frames=200, interval=50)

# Show animation
plt.show()

# Save as GIF (uncomment to save)
# ani.save("beating_heart.gif", writer="pillow", fps=20)
