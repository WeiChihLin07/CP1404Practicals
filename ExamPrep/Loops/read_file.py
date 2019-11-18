"""
Write code to read the guitar.csv and print each part separately with the price formatted like currency
"""

in_file = open("guitar.csv", 'r')
for name, year, price in in_file.readline().strip(','):
    print("{} {} ${}".format(name, year, price))
in_file.close()

# TODO
