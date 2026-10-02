"""
Q9. Student Marks Analyzer
Store marks of multiple students in a list. Using loops, calculate highest
marks, lowest marks, average marks, number of students who passed, and number
who failed. Consider 40 as the passing mark.
"""

marks = [78, 35, 92, 40, 25, 66, 88, 39]

highest = marks[0]
lowest = marks[0]
total = 0
passed = 0
failed = 0

for m in marks:
    if m > highest:
        highest = m
    if m < lowest:
        lowest = m
    total = total + m
    if m >= 40:
        passed = passed + 1
    else:
        failed = failed + 1

average = total / len(marks)

print("Marks:", marks)
print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Students passed:", passed)
print("Students failed:", failed)

