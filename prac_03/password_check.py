"""Write a program that asks the user for a password, with error-checking to repeat if the password
doesn't meet a minimum length set by a variable. The program should then print asterisks as long as the password"""

MINIMUM_LENGTH = 6


def password_check():
    password = input("Enter at least {} characters password: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        password = input("Enter at least {} characters password: ".format(MINIMUM_LENGTH))
    print('*' * len(password))


# password_check()


"""Password checker with functions"""


def main():
    password = get_password(MINIMUM_LENGTH)
    print('*' * len(password))


def get_password(minimum_length):
    password = input("Enter at least {} characters password: ".format(minimum_length))
    while len(password) < minimum_length:
        print("Password does not meet the length requirement.")
        password = input("Enter at least {} characters password: ".format(minimum_length))
    return password


main()
