"""
Q5. Character Frequency Counter
Take a string from the user and calculate how many times each character
occurs. Example: "banana" should identify the frequencies of b, a, and n.
"""

text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] = frequency[ch] + 1
    else:
        frequency[ch] = 1

for ch in frequency:
    print(ch, "=", frequency[ch])
