def main():
    """ Prompts the user for 5 numbers and then stores them in a list"""
    numbers = []
    for number in range(1, 6):
        number = int(input("Number: "))
        numbers.append(number)

    print_number(numbers)


def print_number(numbers):
    """Print numbers in list with built-in function"""
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the number is {}".format(sum(numbers) / len(numbers)))


main()
