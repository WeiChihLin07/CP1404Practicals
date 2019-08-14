def main():
    x = int(input('Enter a first number: '))
    y = int(input('Enter a second number: '))
    print(' (A.)Show the even numbers from x to y \n',
          '(B.)Show the odd numbers from x to y \n',
          '(C.)Show the squares from x to y \n',
          '(Q.)Exit the program')
    choice = input(">>> ").upper()

# Write this section to suit the menu
    while choice != 'Q':
        if choice == 'A':
            for number in range(x, y):
                if number % 2 == 0:
                    print(number)
        elif choice == 'B':
            for number in range(x, y):
                if number % 2 != 0:
                    print(number)
        elif choice == 'C':
            for number in range(x, y):
                    print(number*number)
        else:
            print('Invalid choice')
        choice = input(">>> ").upper()
    print('Finished.')


main()
