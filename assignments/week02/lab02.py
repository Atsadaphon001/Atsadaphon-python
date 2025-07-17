"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""


x = input("1.THB -> USD , 2.USD -> THB = ")
y = float(input("Amount: "))
if x == "1":
    print(f"{y} THB = {y/35.5} USD (Formula: {y} / 35.5)")
elif x == "2":
    print(f"{y} USD = {y*35.5} THB (Formula: {y} * 35.5)")

