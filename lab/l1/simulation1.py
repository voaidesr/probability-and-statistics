import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from numpy import cos, sin, pi

plt.style.use('dark_background')

def draw_circle_and_triangle(ax):
    circle = Circle((0, 0), 1, color='w', linewidth=2, fill=False)
    ax.add_patch(circle)
    ax.plot([cos(-pi/6), cos(pi/2)], [sin(-pi/6), sin(pi/2)], color='w', linewidth=2)
    ax.plot([cos(7* pi /6), cos(pi/2)], [sin(7 * pi/6), sin(pi/2)], color='w', linewidth=2)
    ax.plot([cos(7 * pi/6), cos(-pi/6)], [sin(7*pi/6), sin(-pi/6)], color='w', linewidth=2)

total_lines = 0
total_larger_lines = 0
triangle_length = np.sqrt((cos(-pi/6) - cos(pi/2)) ** 2 + (sin(-pi/6) - sin(pi/2)) ** 2)

def draw_random_segment(ax):
    global total_lines, total_larger_lines, triangle_length

    total_lines += 1
    ang1 = np.random.random() * 2 * pi
    ang2 = np.random.random() * 2 * pi
    length = np.sqrt((cos(ang1) - cos(ang2)) ** 2 + (sin(ang1) - sin(ang2)) ** 2)

    if length >= triangle_length:
        ax.plot([cos(ang1), cos(ang2)], [sin(ang1), sin(ang2)], color='r', linewidth=1, alpha=0.8)
        total_larger_lines += 1
    else:
        ax.plot([cos(ang1), cos(ang2)], [sin(ang1), sin(ang2)], color='y', linewidth=1, alpha=0.8)

    # lungime si tot asa


ax = plt.gca() # axe
ax.set_aspect('equal', 'box')
ax.set_xlim((-1, 1)) # limite la axe
ax.set_ylim((-1, 1))

# pentru fiecare patch este o buna practica sa avem cate o functie separtata
samples = 10000

for _ in range(samples):
    draw_random_segment(ax)

draw_circle_and_triangle(ax)
print("Probability: ", total_larger_lines / total_lines)
# Display the plot
plt.title('Circle and Triangle')
plt.savefig('./img/probability1.svg')