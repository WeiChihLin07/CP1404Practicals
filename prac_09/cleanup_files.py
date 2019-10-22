"""
CP1404/CP5632 Practical
Clean up inconsistent Lyrics file names
"""
import os


def main():
    """Clean up inconsistent Lyrics file names."""
    print("Current directory is", os.getcwd())
    # Change to desired directory
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed version of filename."""
    new_name = filename.replace("", "_").replace(".TXT", ",txt")
    if "_" not in new_name:
        new_name_letters = list(new_name)
        for i, letter in enumerate(new_name_letters):
            if i > 0 and letter.isupper() and new_name_letters[i - 1].isalpha():
                new_name_letters.insert(i, "_")
        new_name = "".join(new_name_letters)
    return new_name


main()
