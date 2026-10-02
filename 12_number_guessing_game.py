"""
Q12. Number Guessing Game
Generate a random number between 1-100. Keep asking the user to guess until
they find the correct number. After each incorrect guess, display "Too High"
or "Too Low". Finally display the number of attempts taken.
"""

import random

secret = random.randint(1, 100)
attempts = 0
guess = 0

while guess != secret:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts = attempts + 1
    if guess > secret:
        print("Too High")
    elif guess < secret:
        print("Too Low")

print("Correct! You guessed the number in", attempts, "attempts")
