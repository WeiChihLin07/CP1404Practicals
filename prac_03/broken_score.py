"""Original broken_score program from prac_01"""


def broken_score():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Pass")
    else:
        print("Bad")


broken_score()
