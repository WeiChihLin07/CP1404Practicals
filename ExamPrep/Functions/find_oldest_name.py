"""
Write code for a function that takes two lists:
1) a list of names
2) a corresponding list of ages
That is, elements at the same list index represent the same person.
The function should return the name of the oldest person in the list.
(Return the first name if multiple people have the same oldest age)
"""


def find_oldest_name(names, ages):
    if ages == []:
        return None
    index_of_oldest = 0
    age_of_oldest = ages[0]
    for i, age in enumerate(ages):
        if age > age_of_oldest:
            index_of_oldest = i
            age_of_oldest = age
    return names[index_of_oldest]
