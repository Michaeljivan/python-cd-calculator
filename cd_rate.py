# Michael Jivan
# CD rate python calculator

# Importing Decimal module for precise floating-point arithmetic
from decimal import Decimal

# CD - Certificate of Deposit
# P - Principal amount
# r - R/100
# R - interest rate
# T - time in years
# n - number of compounding per year

# Formula: CD = P(1 + r/n)^(n*T)

# Taking user inputs
p = Decimal(input("Principal Amount: "))
r = Decimal(input("Interest Rate (%): ")) / Decimal(100)
t = Decimal(int(input("Time in months: ")))/12
n = 12  # Assuming interest compounded monthly

# Calculating CD value
cd = p * (1 + r/n) ** (n*t)

interestGained = round(cd,2) - p
# Displaying the result
print("The value of the Certificate of Deposit (CD) is:", round(cd, 2))
print("Interest earned: ", interestGained)