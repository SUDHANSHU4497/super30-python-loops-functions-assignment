"""
Q4. Find Maximum and Minimum Without max() / min()
Write a program that finds the largest and smallest values in a list using
loops only.
"""

numbers = [45, 12, 78, 3, 56, 89, 23]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Numbers:", numbers)
print("Largest:", largest)
print("Smallest:", smallest)
