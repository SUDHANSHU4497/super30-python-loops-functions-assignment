"""
Q1. Number Analyzer using for loop
Take a number N from the user. Print all numbers from 1 to N, identify whether
each number is even or odd, and finally display the total count of even and
odd numbers.
"""

n = int(input("Enter a number N: "))

even_count = 0
odd_count = 0

for num in range(1, n + 1):
    print(num, sep=', ', end=', ')

for num in range(1, n + 1):
    if num % 2 == 0:
        print(num, "is Even")
        even_count = even_count + 1
    else:
        print(num, "is Odd")
        odd_count = odd_count + 1

print("Total even numbers:", even_count)
print("Total odd numbers:", odd_count)
