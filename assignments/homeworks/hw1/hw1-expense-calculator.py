monthly = float(input("User's monthly income in (THB): "))
rent = float(input("Monthly rent/housing cost: "))
food = int(input("Monthly food budget in (THB): "))
transportation = float(input("Monthly transportation expenses: "))
entertainment = int(input("Monthly entertainment budget: "))
emergency = float(input("Percentage to save for emergency (e.g., 10.5): "))
investment = float(input("Percentage to invest (e.g., 15.0): "))

totalFixed = rent + transportation
totalVariable = food + entertainment
totalExpenses = totalFixed + totalVariable
remaining = monthly - totalExpenses
emergencyAmount = monthly * (emergency / 100)
investmentAmount = monthly * (investment / 100)
available = remaining - emergencyAmount - investmentAmount

expenseRatio = (totalExpenses / monthly) * 100

print("\n=== MONTHLY BUDGET REPORT ===")
print(f"Income: {monthly} THB")
print(f"Fixed Expenses: {totalFixed} THB")
print(f"Variable Expenses: {totalVariable} THB")
print(f"Total Expenses: {totalExpenses} THB")
print(f"Remaining: {remaining} THB")

print("\n=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund ({emergency}%): {emergencyAmount} THB")
print(f"Investment ({investment}%): {investmentAmount} THB")
print(f"Available for Savings: {available} THB")

print("\n=== ANALYSIS ===")
print(f"Expense Ratio: {expenseRatio:.2f}%")