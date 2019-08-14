# Open a file to write
out_file = open("name.txt", 'w')
name = input("Your name: ")
print(name, file=out_file)
out_file.close()

# Open a file to read
in_file = open("name.txt", 'r')
name = in_file.read().strip()
print("Your name is", name)
in_file.close()

# Open 'number.txt' file to read and to display sum of two numbers
in_file = open("numbers.txt", 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

# Open 'number.txt' file to read and to display sum of all numbers
in_file = open("numbers.txt", 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
