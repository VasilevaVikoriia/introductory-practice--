
# ------------------------------------------------------------
print("\n" + "="*50)
print("Exercise 1. Employee ID Card")
print("="*50)

employee_full_name = "Ekaterina Volkova"      # str: employee's full name
employee_age_years = 29                        # int: age in years
employee_monthly_salary = 95000.75             # float: monthly salary in rubles
is_employee_working = True                     # bool: current employment status

print(f"Employee Name: {employee_full_name}")
print(f"Age: {employee_age_years} years")
print(f"Monthly Salary: {employee_monthly_salary:.2f} RUB")
print(f"Currently Working: {is_employee_working}")

# ------------------------------------------------------------
# Exercise 2. Greeting
# Demonstrates: input(), str concatenation, f-string
# ------------------------------------------------------------
print("\n" + "="*50)
print("Exercise 2. Greeting")
print("="*50)

user_name = input("Enter employee's name: ")
user_city = input("Enter employee's city: ")

print(f"Сотрудник {user_name} работает в офисе {user_city}")

# ------------------------------------------------------------
# Exercise 3. Order Cost
# Demonstrates: input(), float(), int(), multiplication
# ------------------------------------------------------------
print("\n" + "="*50)
print("Exercise 3. Order Cost Calculator")
print("="*50)

product_price = float(input("Enter product price (RUB): "))
product_quantity = int(input("Enter quantity: "))

order_total_cost = product_price * product_quantity
print(f"Total order cost: {order_total_cost:.2f} RUB")

# ------------------------------------------------------------
# Exercise 4. Deposit Income
# Demonstrates: input(), float(), percentage calculation
# ------------------------------------------------------------
print("\n" + "="*50)
print("Exercise 4. Deposit Income Calculator")
print("="*50)

deposit_amount = float(input("Enter deposit amount (RUB): "))
deposit_interest_rate = float(input("Enter annual interest rate (%): "))

annual_interest_income = deposit_amount * (deposit_interest_rate / 100)
print(f"Deposit amount: {deposit_amount:.2f} RUB")
print(f"Interest rate: {deposit_interest_rate:.2f}%")
print(f"Annual interest income: {annual_interest_income:.2f} RUB")

# ------------------------------------------------------------
# Exercise 5. Currency Converter (RUB → USD)
# Demonstrates: division, rounding, format specifier
# ------------------------------------------------------------
print("\n" + "="*50)
print("Exercise 5. Currency Converter RUB → USD")
print("="*50)

usd_exchange_rate = float(input("Enter USD exchange rate (RUB per 1 USD): "))
rub_amount_to_convert = float(input("Enter amount in RUB: "))

usd_converted_amount = rub_amount_to_convert / usd_exchange_rate
print(f"{rub_amount_to_convert:.2f} RUB = {usd_converted_amount:.2f} USD")

# ------------------------------------------------------------
# Exercise 6. Profit and Profitability
# Demonstrates: subtraction, division, percentage
# ------------------------------------------------------------
print("\n" + "="*50)
print("Exercise 6. Profit and Profitability Calculator")
print("="*50)

company_revenue = float(input("Enter revenue (RUB): "))
company_costs = float(input("Enter costs (RUB): "))

company_profit = company_revenue - company_costs
profitability_percent = (company_profit / company_revenue) * 100

print(f"Revenue: {company_revenue:.2f} RUB")
print(f"Costs: {company_costs:.2f} RUB")
print(f"Profit: {company_profit:.2f} RUB")
print(f"Profitability: {profitability_percent:.2f}%")

# ------------------------------------------------------------
# Exercise 7. Stock Price Change
# Demonstrates: subtraction, division, multiplication
# ------------------------------------------------------------
print("\n" + "="*50nt("Exercise 7. Stock Price Change Analysis")
print("="*50)

initial_stock_price = float(input("Enter initial stock price (RUB): "))
final_stock_price = float(input("Enter final stock price (RUB): "))

absolute_price_change = final_stock_price - initial_stock_price
percentage_price_change = (absolute_price_change / initial_stock_price) * 100

print(f"Initial price: {initial_stock_price:.2f} RUB")
print(f"Final price: {final_stock_price:.2f} RUB")
print(f"Absolute change: {absolute_price_change:+.2f} RUB")
print(f"Percentage change: {percentage_price_change:+.2f}%")

# ------------------------------------------------------------
# Exercise 8. Mini Price List
# Demonstrates: multiple inputs, string storage, formatted output
# ------------------------------------------------------------
print("\n" + "="*50)
print("Exercise 8. Mini Price List")
print("="*50)

first_product_name = input("Enter first product name: ")
first_product_price = float(input("Enter first product price (RUB): "))

second_product_name = input("Enter second product name: ")
second_product_price = float(input("Enter second product price (RUB): "))

third_product_name = input("Enter third product name: ")
third_product_price = float(input("Enter third product price (RUB): "))

print("\n--- Price List ---")
print(f"Товар: {first_product_name} — {first_product_price:.2f} руб.")
print(f"Товар: {second_product_name} — {second_product_price:.2f} руб.")
print(f"Товар: {third_product_name} — {third_product_price:.2f} руб.")

# ------------------------------------------------------------
# Exercise 9. Annual Budget
# Demonstrates: multiplication, subtraction, multi-line output
# ------------------------------------------------------------
print("\n" + "="*50)
print("Exercise 9. Annual Budget Calculation")
print("="*50)

monthly_income = float(input("Enter monthly income (RUB): "))
monthly_expenses = float(input("Enter monthly expenses (RUB): "))

annual_income_total = monthly_income * 12
annual_expenses_total = monthly_expenses * 12
annual_balance_total = annual_income_total - annual_expenses_total

print(f"Annual income: {annual_income_total:.2f} RUB")
print(f"Annual expenses: {annual_expenses_total:.2f} RUB")
print(f"Annual balance (savings): {annual_balance_total:.2f} RUB")

# ------------------------------------------------------------
# Exercise 10. Invoice with VAT
# Demonstrates: VAT calculation, percentage, multi-step calculation
# ------------------------------------------------------------
print("\n" + "="*50)
print("Exercise 10. Invoice with VAT Calculator")
print("="*50)

product_quantity_vat = int(input("Enter product quantity: "))
product_unit_price = float(input("Enter product unit price (RUB): "))
vat_percent = float(input("Enter VAT rate (%): "))

subtotal_without_vat = product_quantity_vat * product_unit_price
vat_amount = subtotal_without_vat * (vat_percent / 100)
total_with_vat = subtotal_without_vat + vat_amount

print(f"\n--- Invoice ---")
print(f"Quantity: {product_quantity_vat}")
print(f"Unit price: {product_unit_price:.2f} RUB")
print(f"Subtotal (without VAT): {subtotal_without_vat:.2f} RUB")
print(f"VAT ({vat_percent:.0f}%): {vat_amount:.2f} RUB")
print(f"Total (with VAT): {total_with_vat:.2f} RUB")

print("\n" + "="*50)
print("Module 1 Completed! All 10 exercises done.")
print("="*50))
