"""
Q16. Student Grade Function
Create a function that accepts marks for five subjects, calculates total and
percentage, and returns a grade based on rules you define such as A, B, C, D,
or Fail. Add appropriate validation for invalid marks.

Grade rules:
80% and above = A
65% to 79%    = B
50% to 64%    = C
40% to 49%    = D
Below 40%     = Fail
Each mark must be between 0 and 100.
"""


def calculate_grade(marks):
    for m in marks:
        if m < 0 or m > 100:
            return None

    total = 0
    for m in marks:
        total = total + m

    percentage = total / 5

    if percentage >= 80:
        grade = "A"
    elif percentage >= 65:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "Fail"

    return total, percentage, grade


marks = []
for i in range(1, 6):
    m = float(input("Enter marks of subject " + str(i) + ": "))
    marks.append(m)

result = calculate_grade(marks)

if result is None:
    print("Invalid marks! Each mark must be between 0 and 100.")
else:
    total, percentage, grade = result
    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)
