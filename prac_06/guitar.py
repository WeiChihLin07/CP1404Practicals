"""
CP1404/CP5632 Practical - Programming Guitar class
"""
CURRENT_YEAR = 2019
VINTAGE_AGE = 50


class Guitar:
    """Represent Guitar class for storing details of a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Construct a Guitar from the given fields."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string format of a Guitar."""
        return "My guitar: {}, first made in ({}) , worth ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get the age of a guitar based on the CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a Guitar is 50 or more years old."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Less than, used for sorting Guitars - by year released."""
        return self.year < other.year
