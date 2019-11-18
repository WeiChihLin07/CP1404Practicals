"""
Given the existing lists of products,
write a list comprehension to produce a new list containing only the products that are on sale
(True means it's on sale)
"""

products = [["Phone", 340, False], ["PC", 1420.95, True], ["Smartwatch", 250, True]]
products_on_sale = [product[0] for product in products if product[2]]
print(products_on_sale)
