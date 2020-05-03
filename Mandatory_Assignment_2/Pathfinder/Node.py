class Node():

    def __init__(self, x=0, y=0, walkable=True):

        self.x = x
        self.y = y

        self.walkable = walkable

    def __lt__(self, other):

        return self.f < other.f

    def cleanup(self):

        self.h = 0.0

        self.g = 0.0

        self.f = 0.0

        self.opened = 0
        self.closed = False

        self.parent = None

