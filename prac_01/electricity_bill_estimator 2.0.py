TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def main():
    tariff = input('Which tariff? 11 or 31: ')
    daily = float(input('Enter daily use in kwh: '))
    days = int(input('Enter number of billing days: '))
    if tariff == '11':
        total = TARIFF_11 * daily * days
    else:
        total = TARIFF_31 * daily * days
    print("Estimated bill: ${:.2f}".format(total))


main()
