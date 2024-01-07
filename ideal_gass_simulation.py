
'''
    @check:

    https://www.youtube.com/watch?v=tmY6FEF8f1o&ab_channel=KeithGalli


    Python code that animates a 2D ideal gas of particles evolving in a square box. 
    The speeds of the particles at equilibrium follow the Maxwell-Boltzmann distribution. 
    

    Assumptions
    - The particles are represented by circles that all have the same radius and mass.
    - The particles start at random positions and with random velocities.
    - Important: when we initialize our particle positions, we need to make sure that the particles aren't overlapping, otheriwse this can lead to numerical errors. The best way to do this is to arrange them on a grid
    - The number of particles in the container remains fixed throughout the simulation.
    - The particles can collide elastically with each other and the boundaries of the container

'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import product


class IdealGass:

    def __init__(self, N, mass, radius, L, v0, duration, nsteps):
        self.N = N  # number of particles
        self.mass = mass  # mass of particles (kg)
        self.radius = radius  # radius of the particles (m)
        self.L = L  # Length of the box (m)
        self.duration = duration  # duration of the annimation (s)
        self.nsteps = nsteps  # number of steps
        self.dt = duration/nsteps  # timestep (s)
        self.v0 = v0  # initial velocity (m/s)

        # initialize random positions and velocities

        # Need to make sure that the particles are not overlapping

        grid_size = int(np.ceil(np.sqrt(N)))
        spacing = L/grid_size
        x = np.linspace(radius + spacing/2, L - radius - spacing/2, grid_size)
        pos = list(product(x, x))
        self.r = np.array(pos[:N])

        # initialize the velocities
        theta = np.random.uniform(0, 2*np.pi, N)
        vx, vy = v0*np.cos(theta), v0*np.sin(theta)
        self.v = np.stack((vx, vy), axis=1)


N = 20  # Number of particles
mass = 1.0  # kg
radius = 0.2  # m
L = 20  # m
v0 = 3  # m/s
duration = 10  # s
nsteps = 750  # s

gas = IdealGass(N, mass, radius, L, v0, duration, nsteps)
fig = plt.figure()
ax = fig.add_subplot(111)
for (x, y) in gas.r:
    ax.add_artist(plt.Circle((x, y), radius, color='b'))

ax.set_xlim(0, L)
ax.set_ylim(0, L)
ax.set_aspect('equal')
plt.show()
