class Node:
    """ Each node represent a square on the path finding grid"""

    def __init__(self, x=0, y=0, parent=None, walkable=True, h=0, g=0):
        """ Initializer for the Node object
        :param:
            x, y = coordinates of the node
            parent = Node from which we came, used for backtracking path.
            h = distance from starting node
            g = distance to ending node
        """
        self.x = x
        self.y = y

        self.parent = parent

        self.h = h
        self.g = g
        self.f = g + h

        self.walkable = walkable

    def __eq__(self, other):
        """ Dunder method that checks if two points are the same """
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        """ Dunder method that checks if the other nodes f score is larger than this one."""

        return self.f < other.f

    def cleanup(self):
        """ Method to clean up the node when needed """

        self.h = 0.0

        self.g = 0.0

        self.f = 0.0

        self.opened = 0
        self.closed = False

        self.parent = None

