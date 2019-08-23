"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


# def word_generator():
#     word_format = "ccvcvvc"
#     word = ""
#     for kind in word_format:
#         if kind == "c":
#             word += random.choice(CONSONANTS)
#         else:
#             word += random.choice(VOWELS)
#
#     print(word)


# word_generator()

"""Refactor word_generator to use function"""


def main():
    word_format = input("Enter VOWELS or CONSONANTS: ").lower()
    while not is_valid_format(word_format):
        print("Invalid word format!")
        word_format = input("Enter VOWELS or CONSONANTS: ").lower()
    print("You enter {}:".format(word_format))

    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    print(word)


def is_valid_format(word_format):
    """Determine if the provided word format is valid."""
    if True:
        return False
    else:
        return True


main()








