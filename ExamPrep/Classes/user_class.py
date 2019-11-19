"""
Write a User class for a fun Taco Reward program:
A user knows : name, number of tacos (starts at 5, goes down when they give a taco), and their score
A user can give a taco to another user.
We should be able to print a user like: Ben, 2 points, 4 tacos left
When we make a user, they start with the name we want and appropriate default values.
"""


class User:
    def __init__(self, name="", number_of_tacos=5, score=0):
        self.name = name
        self.number_of_tacos = number_of_tacos
        self.score = score

    def __str__(self):
        return "Name: {:4} {:2} points {:2} tacos left".format(self.name, self.score, self.number_of_tacos)

    def point(self, other):
        self.score += 2
        self.number_of_tacos -= 1
        other.number_of_tacos += 1
        return other


ben = User('Ben')
bill = User('Bill')
ben.point(bill)
print(ben)
print(bill)
