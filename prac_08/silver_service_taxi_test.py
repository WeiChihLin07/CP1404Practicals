"""""CP1404/CP5632 Practical - Test SilverServiceTaxi class."""""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi class."""
    taxi = SilverServiceTaxi("Townsville", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.calculate_fare())


main()
