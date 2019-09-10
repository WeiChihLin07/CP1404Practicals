"""CP1404/CP5632 Extension Practical
A program using a dictionary to store the tariffs and the corresponding cost"""

TARIFFS = {"01": 0.244618, "11": 0.136928, "21": 0.213456, "31": 0.109867, "41": 0.318723}


def main():
    for key, value in TARIFFS.items():
        print("TARIFF {} = ${}".format(key, value))
    tariff = input("Which tariff? 01, 11, 21, 31 or 41: ")
    while tariff != "":
        if tariff in TARIFFS:
            daily_use = float(input("Enter daily use in Kwh: "))
            billing_days = int(input("Enter number of billing days: "))
            estimated_bill = (billing_days * daily_use) * TARIFFS[tariff]
            print("Estimated bill: ${:.2f}".format(estimated_bill))
            tariff = input("Which tariff? 01, 11, 21, 31 or 41: ")
        else:
            print("Invalid tariff!")
            tariff = input("Which tariff? 01, 11, 21, 31 or 41: ")

    print("Goodbye!")


main()
