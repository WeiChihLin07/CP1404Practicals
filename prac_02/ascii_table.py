LOWER = 33
UPPER = 127
MIN_COLUMNS = 2
MAX_COLUMNS = 10


def main():
    character = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(character, ord(character)))
    number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
    while number < LOWER or number > UPPER:
        print("Invalid")
        number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
    print("The character for {} is {}".format(number, chr(number)))

    # ASCII table
    for value in range(LOWER, UPPER + 1):
        print("{:3} {:>4}".format(value, chr(value)))

    # ASCII tables with columns
    columns = int(input("Enter number of columns: "))
    while columns < MIN_COLUMNS or columns > MAX_COLUMNS:
        print("Please enter a value between {} and {}".format(MIN_COLUMNS, MAX_COLUMNS))
        columns = int(input("Enter number of columns: "))

    # calculate the range of values and the number of rows
    range_of_values = UPPER - LOWER + 1
    rows = range_of_values // columns

    print("Horizontal then vertical ordering")

    # repeat through the full rows and then incrementing by 1
    value = LOWER
    for row in range(rows):
        for column in range(columns):
            print("{:6} {:>2}".format(value, chr(value)), end='')
            value += 1
        print()

    # handling last row from where we left off and only print up tp UPPER
    beginning_value = value
    for value in range(beginning_value, UPPER + 1):
        print("{:6} {:>2}".format(value, chr(value), end=''))
    print("\n")

    print("Vertical then horizontal ordering")
    # repeat through rows
    for row in range(rows + 1):
        beginning_value = LOWER + row
        value = beginning_value
        # print all column values not including the last one
        for column in range(columns - 1):
            value_to_print = value + (column * rows)
            print("{:6} {:>2}".format(value_to_print, chr(value_to_print)), end='')
            value += 1

        # handle last column separately because it may not exist
        value_to_print = value + ((columns + 1) * rows)
        if value_to_print <= UPPER:
            print("{:6} {:>2}".format(value_to_print, chr(value_to_print)), end='')
        print()


main()
