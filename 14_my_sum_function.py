"""
Q14. Create Your Own sum() Function
Write def my_sum(numbers). It should accept a list of numbers and return their
sum without using Python's built-in sum().
"""


def my_sum(numbers): #number=[1,2,3,4,5]
    total = 0
    for num in numbers:
        total = total + num
    return total


numbers = [10, 20, 30, 40, 50]
result = my_sum(numbers)
print("Numbers:", numbers)
print("Sum:", result)

