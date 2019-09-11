"""
CP1404/CP5632 Practical - Guitars client code.
"""
from prac_06.guitar import Guitar


def play_guitars():
    """Use a list to store all of the user's guitars."""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    if guitars:
        guitars.sort()
        print("These are my guitars: ")
        for i, guitar in enumerate(guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {0}: {1.name:>30}, ({1.year}) worth ${1.cost:,.2f} {2}".format(i + 1, guitar, vintage_string))
    else:
        print("No guitars!")


if __name__ == '__main__':
    play_guitars()
