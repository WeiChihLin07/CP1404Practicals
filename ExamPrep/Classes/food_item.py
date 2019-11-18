"""
Write a class for a food item, with name, calories, gluten-free status
the 'usual' methods for creating and printing an object
a method to get if it is healthy or not (you decide how that works)
"""


class FoodItem:
    def __init__(self, name="", calories=0, gluten_free_status=False):
        self.name = name
        self.calories = calories
        self.gluten_free_status = gluten_free_status

    def __str__(self):
        return "Name: {} Calories: {} Gluten-Free Status: {}".format(self.name, self.calories, self.gluten_free_status)

    def is_healthy(self):
        if self.calories > 130:
            return False
        else:
            return True


cheese_burger = FoodItem("Cheese Burger", 140, False)
print(cheese_burger)
