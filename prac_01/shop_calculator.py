def main():
    number = int(input("Number of items: "))
    while number < 0:
        print("Invalid.")
        number = int(input("Number of items: "))

    total = 0
    for i in range(number):
        price = float(input("Price of item: "))
        total += price

    if total > 100:
        total *= 0.9

    print("Total price for {} items is ${:.2f}".format(number, total))


main()
