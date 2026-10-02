"""
Q13. Menu-Driven Calculator
Build a continuously running calculator using while. Provide Addition,
Subtraction, Multiplication, Division, Modulus, and Exit operations. Handle
division by zero properly.
"""

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "6":
        print("Calculator closed")
        break

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice")
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    elif choice == "3":
        print("Result:", a * b)
    elif choice == "4":
        if b == 0:
            print("Error: Cannot divide by zero")
        else:
            print("Result:", a / b)
    elif choice == "5":
        if b == 0:
            print("Error: Cannot divide by zero")
        else:
            print("Result:", a % b)
