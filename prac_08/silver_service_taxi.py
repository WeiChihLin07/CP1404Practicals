"""""CP1404/CP5632 Practical - SilverServiceTaxi class."""""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi that includes flagfall as class variable."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi that includes fanciness."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string format of a SilverServiceTaxi."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def calculate_fare(self):
        """Calculate the current Taxi fare."""
        return self.flagfall + super().get_fare()
