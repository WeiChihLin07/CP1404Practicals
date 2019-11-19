"""
Write a program that asks the user for a string then displays every letter in the string twice
"""

string = input("String: ")

for char in string:
    print(char * 2, end='')
