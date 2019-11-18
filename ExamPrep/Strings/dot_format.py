"""
Write code to produce:
00
03
06
09
12
"""

for number in range(0, 13, 3):
    print("{:02}".format(number))

"""
Write a print statement using the format method to print like:
name = "Monty"
money = 73.6
Output: Monty has $73.60
"""
name = "Monty"
money = 73.6
print("{} has ${:.2f}".format(name, money))
