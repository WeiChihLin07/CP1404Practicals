"""
Write a function definition to take in a filename and return the longest line of the file.
It should return a tuple of both (line number, length in characters)
Write a function call to show how this would be used.
"""


def main():
    line_number, length = find_longest_line("find_longest_line.py")
    print(line_number, length)


def find_longest_line(filename):
    max_line_number, max_length = 0, 0
    with open(filename, 'r') as in_file:
        for i, line in enumerate(in_file, 1):
            if len(line) > max_length:
                max_length = len(line)
                max_line_number = i
    return max_line_number, max_length


main()
