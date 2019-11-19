"""
Write a Person class that has a name and an age in it
"""


class Person:
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return "Name: {} Age: {}".format(self.name, self.age)


james = Person('James', 23)
print(james)
