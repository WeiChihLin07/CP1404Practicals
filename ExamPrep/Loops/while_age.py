"""
Write a program that asks the user for their age and continues to do so until they enter a valid age
(0 to 150). The program should then display the user's age.
"""

MIN_AGE = 0
MAX_AGE = 150

age = int(input("Age: "))
while age < MIN_AGE or age > MAX_AGE:
    print("Age must between 0 and 150")
    age = int(input("Age: "))
print(age)
