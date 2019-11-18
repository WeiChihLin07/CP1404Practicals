"""
Write a program that asks the user for a string then displays every letter in the string twice.
E.g. if they input "hello exam" it should display "hheelllloo  eexxaamm"
"""

letter = input("Letter: ")
text = ""
for char in letter:
    text += char + char
print(text)
