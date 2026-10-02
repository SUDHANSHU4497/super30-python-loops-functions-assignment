"""
Q7. Prime Number Finder
Ask the user for a starting and ending number. Print all prime numbers within
that range using nested loops.
"""

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Prime numbers between", start, "and", end, ":")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
