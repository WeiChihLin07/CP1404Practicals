def main():
    cents = float(input('Enter cents per Kwh: '))
    daily = float(input('Enter daily use in kwh: '))
    days = int(input('Enter number of billing days: '))
    total = (cents / 100) * daily * days
    print("Estimated bill: $", total)


main()
