
# Variables created by input to plug into calculator function
principal_amount=int(input("What is your principle amount?: "))
rate_amount=int(input("What is your rate of interest?: "))
time_amount=int(input("How long, in years, will you be saving?: "))

# Function to calculate interest
def calculate_interest(principal_amount, rate_amount, time_amount):
    interest = (principal_amount * rate_amount * time_amount) / 100
    return interest

# Output for calculations below
interest = calculate_interest(principal_amount, rate_amount, time_amount,)
print()
# Print statement to show interest accumulated
print(f"The interest for a principal of ${principal_amount:.2f} at {rate_amount}% per year for {time_amount} years is ${interest:.2f}.")
# Print statement to show total in savings after time period
print(f"The total amount in your account at {time_amount} years will be ${principal_amount + interest:.2f}.")
