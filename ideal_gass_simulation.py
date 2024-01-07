
'''
    @check:

    https://www.youtube.com/watch?v=Gn5QoDCDGgo&t=631s&ab_channel=AngryPhysicist


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
        x = np.linspace(radius + spacing/2, L -
                        radius - spacing/2, grid_size)
        pos = list(product(x, x))
        self.r = np.array(pos[:N])

        # initialize the velocities
        theta = np.random.uniform(0, 2*np.pi, N)
        vx, vy = v0*np.cos(theta), v0*np.sin(theta)
        self.v = np.stack((vx, vy), axis=1)

    def check_collisions(self):
        """
            Checks for particle-particle collisions ans particle-wall collisions. 
            If collisions are found, update the velocities of the particles colliding, 
            accounting for the conservation of energy and momentum. 

        """

        r_next = self.r + self.v*self.dt  # position of the particle at the next timestep

        # wall collisions
        # collisions with the left wall
        self.v[r_next[:, 0] < self.radius, 0] *= (-1)
        # collisions with the right wall
        self.v[r_next[:, 0] > self.L - self.radius, 0] *= (-1)
        # collisions on the bottom of the wall
        self.v[r_next[:, 1] < self.radius, 1] *= (-1)
        # collisions on the top of the wall
        self.v[r_next[:, 1] > self.L - self.radius, 1] *= (-1)

        # particle-particle collisions
        for i in range(self.N):
            for j in range(i+1, self.N):
                if np.linalg.norm(r_next[i] - r_next[j]) < 2*self.radius:

                    rdiff = self.r[i] - self.r[j]
                    vdiff = self.v[i] - self.v[j]

                    self.v[i] = self.v[i] - \
                        rdiff.dot(vdiff)/(rdiff.dot(rdiff)) * rdiff
                    self.v[j] = self.v[j] - \
                        rdiff.dot(vdiff)/(rdiff.dot(rdiff)) * rdiff

    def step(self):
        """ Compute the postions at the next timestep. """
        self.check_collisions()
        self.r += self.v*self.dt

    def animate(self):
        """ Animates the ideal gas for the specified number of steps. """
        positions = np.zeros(
            (self.nsteps, N, 2))  # empty array to store positions
        # empty array to store velocity norms
        speeds = np.zeros((self.nsteps, self.N))

        for n in range(self.nsteps):  # iterate through all timesteps
            positions[n, :, :] = self.r  # append positions
            speeds[n:] = np.linalg.norm(self.v, axis=1)  # append to velocities
            self.step()

        return positions, speeds

    def MaxwellBoltzmann(self, v):
        KE_avg = 1/2*self.mass*np.sum(self.v0**2)  # average kinetic energy
        kT = KE_avg  # temperature
        sigma_sq = kT/self.mass  # spread of the distribution
        # Maxwell-Boltzmann distribution
        f = np.exp(-v**2/(2*sigma_sq)) * v/sigma_sq
        return f


N = 20  # Number of particles
mass = 1.0  # kg
radius = 0.2  # m
L = 40  # m
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


positions, speeds = gas.animate()

# check that the total kinetic energy is conserved
np.sum(speeds[0]**2), np.sum(speeds[-1]**2)

v = np.linspace(0, 35, 500)
f = gas.MaxwellBoltzmann(v)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))


def animate_positions(frame):
    ax1.clear()
    ax2.clear()
    for i in range(gas.N):
        x, y = positions[frame, i, 0], positions[frame, i, 1]
        circle = plt.Circle((x, y), gas.radius, fill=True)
        ax1.add_artist(circle)

    ax2.hist(speeds[frame], density=True, bins=25)

    ax1.set_xlabel('$x$', fontsize=15)
    ax1.set_ylabel('$y$', fontsize=15)
    ax1.set_title('Ideal gas animation', fontsize=15)
    ax1.set_xlim(0, gas.L)
    ax1.set_ylim(0, gas.L)
    ax1.set_aspect('equal')
    ax1.set_xticks([])  # remove ticks
    ax1.set_yticks([])

    ax2.set_xlim(0, 15)
    ax2.set_ylim(0, 0.5)
    ax2.set_xlabel('$v$ (m/s)', fontsize=15)
    ax2.set_ylabel('frequency', fontsize=15)
    ax2.set_title('Velocity distribution', fontsize=15)
    ax2.plot(v, f, label='Maxwell-Boltzmann')
    ax2.legend(fontsize=15)

    plt.tight_layout()


interval = duration*1e3/nsteps
animation = FuncAnimation(fig, animate_positions,
                          frames=nsteps, interval=interval)


HTML(animation.to_html5_video())
