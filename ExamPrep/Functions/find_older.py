"""
Given the existing dictionary, write a function that takes 2 parameters:
a dictionary like the given one
an integer threshold age value
The function should return a list of names of the people who are older or equal to the threshold age
"""

THRESHOLD_AGE = 34

name_to_age = {"Bill": 21, "Jane": 34, "Steven": 56}

print(find_older(name, age))


def find_older(name, age):
    return [name for name, age in name_to_age.items() if age >= THRESHOLD_AGE]
