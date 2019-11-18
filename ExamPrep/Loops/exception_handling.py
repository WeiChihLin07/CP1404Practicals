"""
Write a program that asks the user for their age and then prints whether it is odd or even.
The program should not crash if the user enters a non-number (use exception handling)
The program should not allow an invalid age number
Re-prompt until a valid number is entered.
"""

is_valid_input = False
while not is_valid_input:
    try:
        age = int(input("Age: "))
        if age < 0:
            print("Age must be >= 0")
        else:
            is_valid_input = True
            print("even" if age % 2 == 0 else "odd")
    except ValueError:
        print("Invalid (must be an integer)")
