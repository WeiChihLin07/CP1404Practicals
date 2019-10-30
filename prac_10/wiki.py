import wikipedia


def main():
    search_phrase = input("search phrase: ")
    while search_phrase != " ":
        try:
            wikipedia.search(search_phrase)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
    print("{} {} {}".format(search_phrase, wikipedia.summary(search_phrase), search_phrase.url))


main()
