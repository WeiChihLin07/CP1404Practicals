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

    # Security_checker
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
