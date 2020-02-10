class Color:
    """Handles RGB colors on a 0...1 scale.

    Example of a test:

    >>> print(Color(1,0,0) + Color(1,0,0))
    Color(r: 1, g: 0, b: 0)

    """

    def __init__(self, r, g, b):
        """Using max(min(1,x), 0) because we want a number between 0 and 1"""
        self.r = max(min(1, r), 0)
        self.g = max(min(1, g), 0)
        self.b = max(min(1, b), 0)

    def __add__(self, other):
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)

    def __sub__(self, other):
        return Color(self.r - other.r, self.g - other.g, self.b + other.b)

    def __str__(self):
        return f"Color(r: {self.r}, g: {self.g}, b: {self.b})"


if __name__ == "__main__":
    # Only import doctest if this class is the main class
    import doctest

    doctest.testmod()
