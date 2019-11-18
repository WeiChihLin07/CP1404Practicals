"""
Using join method to display output One, Two, Three.
"""

number = 'one two three'.split()
for i in range(len(number)):
    number[i] = number[i].title()
text = ','.join(number)
print(text)
