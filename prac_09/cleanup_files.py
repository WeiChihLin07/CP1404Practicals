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
            new_filename = os.path.join(directory_name, filename)
            fixed_filename = get_fixed_filename(new_filename)
            os.rename(new_filename, fixed_filename)


def get_fixed_filename(filename):
    """Return a 'fixed version of filename."""
    new_name = filename.replace("", "_").replace(".TXT", ".txt")
    old_char = ''
    new_filename = ''
    for character in new_name:
        if old_char.islower():
            if character.isupper():
                new_filename += '_'
        if old_char == '_':
            character = character.upper()
        new_filename += character
        old_char = character
    return new_filename


main()
