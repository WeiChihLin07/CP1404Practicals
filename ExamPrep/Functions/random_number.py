"""
Write a function that takes in one integer parameter n,
and return a list of n unique random numbers between 1 and 10 * n
"""

import random


def main():
    n = 5
    print(find_random_number(n))


def find_random_number(n):
    random_numbers = []
    for i in range(n):
        number = random.randint(1, 10 * n)
        while number in random_numbers:
            number = random.randint(1, 10 * n)
        random_numbers.append(number)
    return random_numbers


main()
