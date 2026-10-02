"""
Q18. Employee Salary Calculator
Create a function that accepts employee name, basic salary, bonus percentage,
and tax percentage. Calculate gross salary, tax amount, and final salary.
Process at least five employees using a loop.
"""


def calculate_salary(name, basic_salary, bonus_percent, tax_percent):
    bonus = basic_salary * bonus_percent / 100
    gross_salary = basic_salary + bonus
    tax_amount = gross_salary * tax_percent / 100
    final_salary = gross_salary - tax_amount
    return gross_salary, tax_amount, final_salary


employees = [
    ["Aarav", 30000, 10, 5],
    ["Priya", 45000, 12, 10],
    ["Rohan", 25000, 8, 5],
    ["Sneha", 60000, 15, 20],
    ["Vikram", 38000, 10, 10],
]

for emp in employees:
    name = emp[0]
    basic = emp[1]
    bonus_percent = emp[2]
    tax_percent = emp[3]

    gross, tax, final = calculate_salary(name, basic, bonus_percent, tax_percent)

    print("\nName:", name)
    print("Basic Salary:", basic)
    print("Gross Salary:", gross)
    print("Tax Amount:", tax)
    print("Final Salary:", final)

