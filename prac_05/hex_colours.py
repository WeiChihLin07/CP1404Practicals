"""A program that allows to look up hexadecimal colour codes"""
HEXADECIMAL_COLOURS = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aquamarine1": "#7fffd4", "azure1": "#f0ffff",
                       "beige": "#f5f5dc", "black": "#000000", "blanchedalmond": "#ffebcd", "blueviolet": "#8a2be2",
                       "brown": "#a52a2a", "burlywood": "#deb887", "cadetblue": "#5f9ea0"}


def main():
    colour_name = input("Enter colour name: ").lower()
    while colour_name != "":
        if colour_name in HEXADECIMAL_COLOURS:
            print("{} is {}".format(colour_name, HEXADECIMAL_COLOURS[colour_name]))
        else:
            print("Invalid colour name")
        colour_name = input("Enter colour name: ").lower()


main()
