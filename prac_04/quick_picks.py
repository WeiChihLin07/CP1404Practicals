import random
RANDOM_NUMBER = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    numbers_of_picks = []
    number_of_picks = int(input("How many quick picks? "))

    for number in range(number_of_picks):
        numbers = random.randint(MIN_NUMBER, MAX_NUMBER)
        numbers_of_picks.append(numbers)
        print(numbers_of_picks)


main()
