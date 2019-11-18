"""
Write client code for your food item, that gets the values from a user until they enter a blank name
creates a food object for each item and adds it to a list prints all of the "healthy" items in the list
using a list comprehension
"""

from ExamPrep.Classes.food_item import FoodItem

item_name = input("Item Name: ")
food_items = []
while item_name != "":
    calories = int(input("Calories: "))
    gluten_free = input("Gluten_Free: Yes or No: ").title()
    food_items.append(FoodItem(item_name, calories, gluten_free))
    item_name = input("Item Name: ")
healthy_items = [food_item.name for food_item in food_items if food_item.is_healthy()]
print(healthy_items)
