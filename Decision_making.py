# This is a program to determine whether your age qualifies for certain age..
# restricted benefits

# User input for age
user_age=int(input('What is your age?: '))

# Statement to determine if old enough to drive
if user_age >= 16:
    print("You are old enough to drive.")
else:
     print("You are too young to drive.")

# Statement to determine if old enough to vote
if user_age >= 18:
     print("You are old enough to vote.")
else:
     print("You are too young to vote.")

# Statement to determine if old enough to drink
if user_age >= 21:
     print("You are old enough to drink.")
else:
     print("You are too young to drink.")

# Statement to determine senior citizen eligibility
if user_age >= 65:
     print("You qualify for Senior Citizen discounts.")
else:
     print("You are too young to qualify for Senior Citizen discounts.")

# Output determines what user age qualifies for