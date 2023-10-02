# 3.3 Conditional Code
# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

def get_letter_grade(score_float):
    if score_float >= 0.9:
        print("A")
    elif score_float >= 0.8:
        print("B")
    elif score_float >= 0.7:
        print("C")
    elif score_float >= 0.6:
        print("D")
    else:
        print("F")

def check_given_score(decimal):
    score_str = input("Enter Score: ")
    score_float = float(score_str)
    x = 0.0
    y = 1.0
    if score_float < x or score_float > y:
        print("Error. Please put a score between 0.0 and 1.0.")
    elif score_float >= x and score_float <= y:
        get_letter_grade(score_float)

check_given_score(input)
