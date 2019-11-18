"""
Write a program that swaps the content of a file, "switch.txt" between "out" and "in" every time it runs
"""

with open("switch.txt", 'r') as in_file:
    text = in_file.read().strip()
    if text == "out":
        text = 'in'
    else:
        text = 'out'

with open("switch.txt", 'w') as out_file:
    out_file.write(text)
