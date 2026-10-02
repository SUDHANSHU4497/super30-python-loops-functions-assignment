"""
Q19. Bank Account Mini Application
Create functions for deposit(), withdraw(), check_balance(), and
transaction_history(). Use a while loop to keep the banking application
running. Prevent withdrawals when sufficient balance is unavailable.
"""

balance = 0
history = []


def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance = balance + amount
        history.append("Deposited ₹" + str(amount))
        print("Deposit successful")
    else:
        print("Invalid amount")


def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Invalid amount")
    elif amount > balance:
        print("Insufficient balance")
    else:
        balance = balance - amount
        history.append("Withdrew ₹" + str(amount))
        print("Withdrawal successful")


def check_balance():
    print("Current balance: ₹", balance)


def transaction_history():
    if len(history) == 0:
        print("No transactions yet")
    else:
        for t in history:
            print(t)


while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        deposit()
    elif choice == "2":
        withdraw()
    elif choice == "3":
        check_balance()
    elif choice == "4":
        transaction_history()
    elif choice == "5":
        print("Thank you for banking with us")
        break
    else:
        print("Invalid choice")
