class LinearFunction:
    """Class representing a linear function y = mx + b."""

    m: float
    b: float

    def __init__(self, m: float, b: float):
        """Initializes the class."""
        self.m = m
        self.b = b
