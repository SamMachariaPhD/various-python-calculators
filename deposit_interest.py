# Constants
amount = 1000000  # Amount in KES
interest_rate = 0.1125  # Interest rate (11.25%)
tax_rate = 0.15  # Tax rate (15%)
months = 12  # Number of months
currency = "KES"

# Calculate interest for the specified number of months
interest = amount * interest_rate * (months / 12)

# Calculate tax on interest
tax = interest * tax_rate

# Calculate interest after tax
interest_after_tax = interest - tax

# Calculate total amount after deducting tax
total_amount = amount + interest - tax

# Output results
print(f"Amount: {amount} {currency}")
print(f"Interest for {months} months: {interest} {currency}")
print(f"Tax on Interest: {tax} {currency}")
print(f"Interest after Tax: {interest_after_tax} {currency}")
print(f"Total Amount after Tax: {total_amount} {currency}")

