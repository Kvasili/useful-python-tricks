
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


class IdealGass():

    def __init__(self, x, y):
        pass
