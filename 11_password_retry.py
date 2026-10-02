"""
Q11. Password Retry System
Store a predefined password and give the user a maximum of three attempts to
enter it correctly. Use a while loop. After three incorrect attempts, display
"Account Locked".
"""

password = "super30"
attempts = 0

while attempts < 3:
    entered = input("Enter password: ")
    if entered == password:
        print("Login successful")
        break
    else:
        attempts = attempts + 1
        print("Wrong password. Attempts left:", 3 - attempts)

if attempts == 3:
    print("Account Locked")
