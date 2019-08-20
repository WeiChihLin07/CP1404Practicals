"""Write a program that asks the user for a password, with error-checking to repeat if the password
doesn't meet a minimum length set by a variable. The program should then print asterisks as long as the password"""

MINIMUM_LENGTH = 6


def main():
    password = input("Enter at least {} characters password: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        password = input("Enter at least {} characters password: ".format(MINIMUM_LENGTH))
    print('*' * len(password))


main()
