"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# print(STATE_NAMES)

state = input("Enter short state: ").upper()
while state != "":
    if state in STATE_NAMES:
        print("{} is {}".format(state, STATE_NAMES[state]))
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()

# Write a loop that prints all of the states and names neatly lined up with string formatting
for state in STATE_NAMES:
    print("{:3} is {:12}".format(state, STATE_NAMES[state]))
