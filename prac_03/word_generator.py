"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

"""Refactor word_generator to use function"""


def main():
    word_format = input("Enter VOWELS or CONSONANTS: ").lower()
    while not is_valid_format(word_format):
        print("Invalid word format!")
        word_format = input("Enter VOWELS or CONSONANTS: ").lower()
    print("You enter {}:".format(word_format))

    word = ""
    for kind in word_format:
        if kind in VOWELS:
            word += random.choice(VOWELS)
        else:
            word += random.choice(CONSONANTS)

    print(word)


def is_valid_format(word_format):
    """Determine if the provided word format is valid."""
    count_vowel = 0
    count_consonant = 0
    count_digit = 0
    count_special = 0
    for char in word_format:
        if char in VOWELS:
            count_vowel += 1
        elif char in CONSONANTS:
            count_consonant += 1
        elif char.isdigit():
            count_digit += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1

    if count_vowel == 0 or count_consonant == 0 or count_digit >= 1 or count_special >= 1:
        return False
    else:
        return True


main()
