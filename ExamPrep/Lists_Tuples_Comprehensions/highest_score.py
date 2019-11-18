"""
Write a program that asks the user for their scores and adds them to the list,
until they enter a negative score, then prints their highest score.
"""

scores = []
is_valid_input = False
while not is_valid_input:
    try:
        score = int(input("Score: "))
        if score < 0:
            print("Score must be >= 0")
        else:
            is_valid_input = True
            while score >= 0:
                scores.append(score)
                score = int(input("Score: "))
    except ValueError:
        print("Not an integer")
print("Your highest score is", max(scores))
