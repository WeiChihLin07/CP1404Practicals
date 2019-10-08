"""""CP1404/CP5632 Practical - Test UnreliableCar client code."""""

from prac_08.unreliable_car import UnreliableCar


def main():
    """Test examples of UnreliableCars."""
    toyota_rav4 = UnreliableCar("Reliable", 100, 90)
    nissan_tida = UnreliableCar("Unreliable", 100, 10)

    # simulate number of times both cars drive and output the driven distance
    for number in range(1, 15):
        print("{} attempt to drive:".format(number))
        print("{:20} drove {:6}km".format(toyota_rav4.name, toyota_rav4.drive(number)))
        print("{:20} drove {:6}km".format(nissan_tida.name, nissan_tida.drive(number)))

    # display the final status of both cars
    print(toyota_rav4)
    print(nissan_tida)


main()
