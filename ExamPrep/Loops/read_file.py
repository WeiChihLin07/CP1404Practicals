"""
Write code to read the guitar.csv and print each part separately with the price formatted like currency
"""

with open("guitar.csv", 'r') as in_file:
    for line in in_file:
        guitar = line.strip().split(',')
        print("{:20} {:4} ${:.2f}".format(guitar[0], guitar[1], float(guitar[2])))
