# code the wave particle duality of light photons using broglie's equation

# import packages
import matplotlib.pyplot as plt
import numpy as np


# define the function
def broglie(frequency):
    return 6.62607004e-34 / frequency


def wavelength(frequency):
    return 3e8 / frequency


def energy(frequency):
    return 6.62607004e-34 * frequency


def wave_particle_duality(frequency):
    return 6.62607004e-34 / frequency * 3e8 / frequency


# define the grid
x = np.linspace(1e14, 1e15, 100)
y = np.linspace(1e14, 1e15, 100)
X, Y = np.meshgrid(x, y)

# calculate the function value
Z = wave_particle_duality(X)

# plot the function
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
ax.set_xlabel('frequency')
ax.set_ylabel('frequency')
ax.set_zlabel('wave particle duality')
ax.set_title('Wave Particle Duality of Light Photons')
ax.view_init(30, 30)
ax.set_zlim(0, 1e-43)
ax.set_xlim(1e14, 1e15)
ax.set_ylim(1e14, 1e15)
ax.set_zticks([0, 0.5e-43, 1e-43])
ax.set_xticks([1e14, 1e14, 1e15])
ax.set_yticks([1e14, 1e14, 1e15])
plt.show()
