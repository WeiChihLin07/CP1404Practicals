"""
Write a function to count the letters in string.
(i.e. count alphabetical letters, not characters)
Check if each character is a member of string.ascill_lowercase
Use char.lower() to ignore case
"""


def main():
    text = input("Text: ")
    print(count_letters(text))


def count_letters(string):
    count = 0
    for char in string:
        if char.isalpha():
            count += 1
    return count


main()
