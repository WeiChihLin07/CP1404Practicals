"""
Write client code for your food item, that gets the values from a user until they enter a blank name
creates a food object for each item and adds it to a list prints all of the "healthy" items in the list
using a list comprehension
"""

# ToDo

from ExamPrep.Classes.food_item import FoodItem

name = input("Name: ")
while name != "":
    calories = int(input("Calories: "))
    gluten_free_status = input("True or False: ").title()
    name = input("Name: ")
    food_items = []
    food_items.append(FoodItem(name, calories, gluten_free_status))
    print(FoodItem for FoodItem in food_items if FoodItem.is_healthy())
print("Bye")
