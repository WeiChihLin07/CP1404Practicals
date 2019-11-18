"""
Write code to read the guitar.csv and print each part separately with the price formatted like currency
"""

with open("guitar.csv", 'r') as in_file:
    for line in in_file:
        guitar = line.strip(',')
    print(guitar)

# TODO
