"""CP1404/CP5632 Practical - Sort files based on extension"""

import os


def main():
    """Move files into folders with the same name as their extension."""
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]

        # Try making folders and ignore errors (EAFP)
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        print("{}/{}".format(extension, filename))
        os.rename(filename, "{}/{}".format(extension, filename))


main()
