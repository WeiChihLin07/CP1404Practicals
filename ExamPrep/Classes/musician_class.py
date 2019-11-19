"""
Write a Musician class - derived from Person, also has play(duration) method
"""

from ExamPrep.Classes.person_class import Person


class Musician(Person):
    def __init__(self, name='', age=0):
        super().__init__(name, age)
        self.wages = wages

    def __str__(self):
        return "{}".format(super().__str__())

    def play(self, duration):
        hourly_rate = 25.50
        self.wages = duration * hourly_rate
        return self.wages


# TODO:

lindsay = Musician('Lindsay', 42)
print(lindsay)
lindsay.play(10)
