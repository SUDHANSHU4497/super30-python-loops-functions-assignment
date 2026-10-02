"""
Q10. ATM Withdrawal Simulator using while
Start with a balance of Rs.10,000. Continuously show the user options to check
balance, deposit money, withdraw money, or exit. The program should continue
until the user explicitly chooses Exit.
"""

balance = 10000

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is ₹", balance)

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance = balance + amount
            print("Deposited successfully. New balance is ₹", balance)
        else:
            print("Invalid amount")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount")
        elif amount > balance:
            print("Insufficient balance")
        else:
            balance = balance - amount
            print("Please collect your cash. Remaining balance is ₹", balance)

    elif choice == "4":
        print("Thank you for using the ATM")
        break

    else:
        print("Invalid choice")
