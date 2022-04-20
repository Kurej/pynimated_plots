# Import packages
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from fermi import fermi

save_flag = True

# General plot parameters
mpl.rcParams['font.family'] = 'Avenir'
mpl.rcParams['font.size'] = 18
mpl.rcParams['axes.linewidth'] = 2
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['xtick.major.size'] = 10
mpl.rcParams['xtick.major.width'] = 2
mpl.rcParams['ytick.major.size'] = 10
mpl.rcParams['ytick.major.width'] = 2


# Create figure and add axes
fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(111)

# Temperature values
T = np.linspace(100, 1000, 10)

# Get colors from coolwarm colormap
colors = plt.get_cmap('coolwarm', 10)

# Plot F-D data
for i in range(len(T)):
    x = np.linspace(0, 1, 100)
    y = fermi(x, 0.5, T[i])
    ax.plot(x, y, color=colors(i), linewidth=2.5)

# Add legend
labels = ['100 K', '200 K', '300 K', '400 K', '500 K', '600 K', 
          '700 K', '800 K', '900 K', '1000 K']
ax.legend(labels, bbox_to_anchor=(1.05, -0.1), loc='lower left', 
          frameon=False, labelspacing=0.2)



# Import animation package
from matplotlib.animation import FuncAnimation

# Change matplotlib backend (if using Jupyter notebook)
# %matplotlib notebook

# Create variable reference to plot
f_d, = ax.plot([], [], linewidth=2.5)

# Add text annotation and create variable reference
temp = ax.text(1, 1, '', ha='right', va='top', fontsize=24)

# Animation function
def animate(i):
    x = np.linspace(0, 1, 100)
    y = fermi(x, 0.5, T[i])
    f_d.set_data(x, y)
    f_d.set_color(colors(i))
    temp.set_text(str(int(T[i])) + ' K')
    temp.set_color(colors(i))

# Create animation
ani = FuncAnimation(fig=fig, func=animate, frames=range(len(T)), interval=500, repeat=True)

# Ensure the entire plot is visible
fig.tight_layout()

# Save or show animation
if save_flag:
    ani.save('./outputs/AnimatedPlot.gif', writer='imagemagick', fps=2)
else:
    plt.show()
