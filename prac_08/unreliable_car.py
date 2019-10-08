"""CP1404/CP5632 Practical - UnreliableCar class."""

from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """""Initialise a UnreliableCar instance, based on parent class Car."""""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if number is less than the car's reliability."""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
