"""CP1404/CP5632 Practical - TaxiSimulator."""

from prac_06.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = """
q)uit, c)hoose taxi, d)rive"""


def main():
    """taxi_simulator to use Taxi and SilverServiceTaxi classes."""
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            print(taxis)
            distance_to_drive = int(input("How many km do you wish to drive? "))
            while distance_to_drive < 0:
                print("Distance must be >= 0")
                distance_to_drive = int(input("How many km do you wish to drive? "))
            distance_driven = car.drive(distance_to_drive)
            print("The car drove {}km".format(distance_driven), end="")
            if car.fuel == 0:
                print(" and ran out of fuel", end="")
            print(".\n")
        elif choice == "d":
            distance_to_drive = int(input("Drive how far?"))

            fuel_to_add = int(input("How many units of fuel do you want to add to the car? "))
            while fuel_to_add < 0:
                print("Fuel amount must be >= 0")
                fuel_to_add = int(input("How many units of fuel do you want to add to the car? "))
            car.add_fuel(fuel_to_add)
            print("Added {} units of fuel.".format(fuel_to_add))
        else:
            print("Invalid choice\n")
        print(car)
        print(MENU)
        choice = input("Enter your choice: ").lower()
    print("\nGood bye {}'s driver".format(car.name))


main()
