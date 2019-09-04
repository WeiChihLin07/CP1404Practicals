def main():
    numbers = [3, 1, 4, 1, 5, 9, 2]
    print(numbers[0],
          numbers[-1],
          numbers[3],
          numbers[:-1],
          numbers[3:4],
          5 in numbers,
          7 in numbers,
          "3" in numbers,
          numbers + [6, 5, 3], sep="\n")

    # Change the first element of numbers to "ten"
    numbers[0] = "ten"
    print(numbers[0])

    # Change the last element of numbers to 1
    numbers[-1] = 1
    print(numbers[-1])

    # Get all the elements from numbers except the first two
    print(numbers[1:-1])

    # Check if 9 is an element of numbers
    print(9 in numbers)


main()
