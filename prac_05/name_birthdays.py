"""
CP1404/CP5632 Extension Practical
A function that takes two parallel lists as input parameters and returns a dictionary where keys are from
the first list and the values are from the second.
"""


def main():
    names = ["Jake", "Jill", "Harry"]
    dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]
    names_birthdays = convert_list_to_dict(names, dates_of_birth)
    print(names_birthdays)


def convert_list_to_dict(list1, list2):
    names_birthdays = {}
    for num, i in enumerate(list1):
        names_birthdays[i] = list2[num]
    return names_birthdays


main()
