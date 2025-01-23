
print("lets calculate your monthly mortgage payment ")
amount_to_borrowed = float(input("How much are you borrowing? $ "))
interest_rate = float(input("annual interest rate? (%) "))
years_to_repay = int(input("how many years will it take you to repay? "))

monthly_rate = (interest_rate / 100) / 12
total_months = years_to_repay * 12


monthly_payment = (amount_to_borrowed * monthly_rate * (1 + monthly_rate)**total_months / ((1 + monthly_rate)** total_months - 1))

print(f"Your monthly payment amount will be: ${monthly_payment}")