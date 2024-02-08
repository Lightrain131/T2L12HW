# Import library
import numpy as n
import matplotlib.pyplot as p

# INTERACTIVE MODE ON
p.ion()

# Create the graph
p.figure(figsize=(5, 5))
ax = p.gca()
p.grid()

# Limit the rate between axes
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_aspect('equal', 'box')

# Unit circle
circle = n.linspace(0, 2 * n.pi, 100)

# Draw
for t in circle:
    x = n.cos(t)
    y = n.sin(t)
    p.plot(x, y, 'b.')
    p.axvline(color='black')
    p.axhline(color='black')
    p.pause(0.01)

# Show
p.show(block=True)

# QUIT
quit()
