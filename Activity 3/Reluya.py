# Prompt the user for hours and rate per hour
hour = 8
rate = 380

hours = float(input("Enter Hours: "))
rate_per_hour = float(input("Enter Rate per Hour: "))

# Compute gross pay
gross_pay = hours * rate_per_hour

# Print the result
print("Pay:", gross_pay)
