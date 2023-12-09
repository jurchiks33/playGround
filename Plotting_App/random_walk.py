from random import choice

class RabdomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes to walk."""
        self.num_points = num_points

        #All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""
        #Keep walking while desired lenght is reached.

        #Decide which direction to go.
        x_direction = choice([1, -1])
        x_distance = choice([0, 1, 2, 3, 4])
        x_step = x_direction * x_distance