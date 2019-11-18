"""
Ask the user to guess a number between 1 and 10 and keep asking until they get it right.
Use a CONSTANT for the secret number
"""

SECRET_NUMBER = 6

number = int(input("Guess a number between 1 and 10: "))
while number != SECRET_NUMBER:
    print("Wrong")
    number = int(input("Number must between 1 and 10: "))
print("Correct")
