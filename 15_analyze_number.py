"""
Q15. Reusable Number Analysis Function
Create a function def analyze_number(number): ... It should determine whether
the number is positive/negative/zero, even/odd, and prime/not prime. Return
the results rather than only printing them.
"""


def analyze_number(number):
    if number > 0:
        sign = "Positive"
    elif number < 0:
        sign = "Negative"
    else:
        sign = "Zero"

    if number % 2 == 0:
        even_odd = "Even"
    else:
        even_odd = "Odd"

    prime = "Prime"
    if number < 2:
        prime = "Not Prime"
    else:
        for i in range(2, number):
            if number % i == 0:
                prime = "Not Prime"
                break

    return sign, even_odd, prime


num = int(input("Enter a number: "))
sign, even_odd, prime = analyze_number(num)

print("Number:", num)
print("Sign:", sign)
print("Even/Odd:", even_odd)
print("Prime:", prime)
