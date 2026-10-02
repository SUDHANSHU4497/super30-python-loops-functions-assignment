"""
Q2. Multiplication Table Generator
Take a number from the user and print its multiplication table from 1 x N
through 10 x N using a for loop. Then modify the program so the ending range
can also be supplied by the user.
"""

num = int(input("Enter a number: "))

print("Table from 1 to 10:")
for i in range(1, 11):
    print(i, "x", num, "=", i * num)

end = int(input("Enter the ending range: "))

print("Table from 1 to", end, ":")
for i in range(1, end + 1):
    print(i, "x", num, "=", i * num)
