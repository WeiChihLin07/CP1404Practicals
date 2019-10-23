"""CP1404/CP5632 Practical - TaxiSimulator.
Write a taxi simulator program that uses your Taxi and SilverServiceTaxi classes.
Each time, until they quit:
The user should be presented with a list of available taxis and get to choose one.
Then they should say how far they want to drive.
At the end of each trip, show them the price and add it to their bill."""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """taxi_simulator to use Taxi and SilverServiceTaxi classes."""
    total_bill = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = get_valid_taxi_choice(taxis)
            current_taxi = taxis[taxi_choice]
        elif choice == "d":
            if current_taxi is not None:
                current_taxi.start_fare()
                distance_to_drive = get_valid_distance_to_drive()
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_cost))
                total_bill += trip_cost
        else:
            print("Invalid choice")
        print("Bill to date: ${:.2f}".format(total_bill))
        print(MENU)
        choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now: ")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display corresponding taxis in the list with index number."""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def get_valid_taxi_choice(taxis):
    """Validate input, ensuring it cannot be empty string and must be within boundary points."""
    is_valid_taxi_choice = False
    while not is_valid_taxi_choice:
        try:
            taxi_choice = int(input("Choose taxi: "))
            if taxi_choice < 0:
                print("Number must be >= 0")
            elif taxi_choice > len(taxis) - 1:
                print("Invalid taxi choice")
            else:
                is_valid_taxi_choice = True
        except ValueError:
            print("Invalid input; enter a valid number.")
    return taxi_choice


def get_valid_distance_to_drive():
    """Validate input, ensuring it cannot be empty string and is only digits and greater than 0."""
    is_valid_distance_to_drive = False
    while not is_valid_distance_to_drive:
        try:
            distance_to_drive = float(input("Drive how far? "))
            if distance_to_drive < 1:
                print("Number must be > 0")
            else:
                is_valid_distance_to_drive = True
        except ValueError:
            print("Invalid input; enter a valid number.")
    return distance_to_drive


main()
