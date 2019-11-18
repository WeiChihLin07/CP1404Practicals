"""
Write a program to calculate the average age of a group of people, of unknown size.
Use a negative number as the 'sentinel' (when to stop)
"""

number_of_people = 0
total = 0
age = int(input("Age: "))
while age > 0:
    number_of_people += 1
    total += age
    age = int(input("Age: "))

if number_of_people == 0:
    print("Not defined")
else:
    print(total / number_of_people)
