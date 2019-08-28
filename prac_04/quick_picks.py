""" Quick pick program
    choose sets of random numbers"""

import random

NUMBERS_IN_ROW = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    number_of_picks = int(input("How many quick picks? "))
    while number_of_picks <= 0:
        print("Invalid!")
        number_of_picks = int(input("How many quick picks? "))

    for number in range(number_of_picks):
        quick_pick = []
        for pick_row in range(NUMBERS_IN_ROW):
            generate_number = random.randint(MIN_NUMBER, MAX_NUMBER)
            while generate_number in quick_pick:
                generate_number = random.randint(MIN_NUMBER, MAX_NUMBER)
            quick_pick.append(generate_number)
        quick_pick.sort()

        # generator expression with join method
        print(" ".join("{:2}".format(generate_number) for generate_number in quick_pick))


main()
