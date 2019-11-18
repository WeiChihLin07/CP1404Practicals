"""
Write Python code to ask the user for their age, then print the square of each each number from
that age down to zero
"""

age = int(input("Age: "))
for i in range(age, -1, -1):
    print(i ** 2)

print("----------------------")
"""
Write a for loop that prints Olympic years (every 4 years) from 1900 to now
"""

for year in range(1900, 2020, 4):
    print(year)

"""
Write a function that takes two integer input parameters, adds up the numbers between these (inclusive) and returns the total.
If the first number is not less than the second number it should return 0. 
Example if the parameters are (9, 11), it should return 30
"""


def main():
    x = 9
    y = 11
    print(calculate_number(x, y))


def calculate_number(x, y):
    total = 0
    if x > y:
        return "0"
    else:
        for number in range(x, y + 1):
            total += number
        return total


main()
