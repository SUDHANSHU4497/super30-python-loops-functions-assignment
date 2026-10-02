"""
Q3. Sum and Average Without sum()
Given a list of numbers, calculate the total and average using a loop.
Do not use Python's built-in sum() function.
"""

numbers = [10, 20, 30, 40, 50]

total = 0
for num in numbers:
    total = total + num

average = total / len(numbers)

print("Numbers:", numbers)
print("Total:", total)
print("Average:", average)
