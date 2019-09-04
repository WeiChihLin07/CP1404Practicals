"""This program count the occurrences of words in a string.
    The program should ask the user for a string, then print the counts of how many of each word are in the file."""


def main():
    words_dict = {}
    sentence = input("Enter a sentence: ")

    words = sentence.split()

    # word is the value of the Key: Value pairs
    for word in words:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1

    # words = list(words_dict.keys())
    # words.sort()
    words = sorted(words_dict.keys())

    # Using longest word for .format to format nicely
    longest_word = max(len(word) for word in words)
    for word in words:
        print("{:{}} : {}".format(word, longest_word, words_dict[word]))


main()
