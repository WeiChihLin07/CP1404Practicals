"""
Ask the user for their name
Tell them how many vowels are in their name
Example output:
Name: Bobby McAardvark
Out of 16 letters, Bobby MaAardvark has 4 vowels
Use the str.format() method for the last print
"""

VOWELS = "aeiou"
name_in_vowels = 0
name = input("Name: ")
for char in name:
    if char.lower() in VOWELS:
        name_in_vowels += 1
print("Out of {} letters, {} has {} vowels".format(len(name), name, name_in_vowels))
