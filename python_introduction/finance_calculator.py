monthly_income = float(input("Enter your monthly income: "))
total_expenses = float(input("Enter your total expenses: "))
monthly_savings = monthly_income - total_expenses
annual_interest_rate = 0.05
projected_unnual_savings = (monthly_savings * 12) * (1 + annual_interest_rate)
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")