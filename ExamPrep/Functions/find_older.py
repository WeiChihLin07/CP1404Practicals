"""
Given the existing dictionary, write a function that takes 2 parameters:
a dictionary like the given one
an integer threshold age value
The function should return a list of names of the people who are older or equal to the threshold age
"""


def main():
    names_to_ages = {"Bill": 21, "Jane": 34, "Sven": 56}
    print(find_older(names_to_ages, 30))
    print(find_elder(names_to_ages, 20))


def find_older(names_to_ages, threshold_age):
    """ for loop"""
    older_people = []
    for name in names_to_ages:
        if names_to_ages[name] >= threshold_age:
            older_people.append(name)
    return older_people


def find_elder(names_to_ages, threshold_age):
    """list comprehension"""
    elder_people = [name for name in names_to_ages if names_to_ages[name] >= threshold_age]
    return elder_people


main()
