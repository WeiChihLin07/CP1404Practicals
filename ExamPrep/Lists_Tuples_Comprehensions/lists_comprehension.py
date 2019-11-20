"""
1) Write a list comprehension with all unhealthy food
2) Write a list comprehension with food price under 3.00
3) Write a list comprehension with food starts with A
"""

foods = [["Burger", 6.50, False], ["Apple", 1.00, True], ["Pizza", 3.00, False]]

print([food[0] for food in foods if not food[2]])

print([food[0] for food in foods if food[1] < 3])

print([food[0] for food in foods if food[0].startswith("A")])

print([food[0] for food in foods if food[0][0] == "A"])
