"""
Write a function to count the number of words in a string (ignoring punctuation),
e.g. s = "This is a sentence with words in it"
print(count_words(s)) # displays 8
"""


def main():
    s = "This is a sentence with words in it"
    print(count_words(s))


def count_words(string):
    words = string.split(' ')
    return len(words)


main()
