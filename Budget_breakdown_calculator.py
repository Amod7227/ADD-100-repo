# This is a program to help you calculate your monthly budget and expenses

# This variable is created by user input for monthly income 
income=float(input("What is your monthly income?: "))

# This variable is created by user input for monthly mortgage payment
mortgage=float(input("What is your monthly mortgage payment amount?: "))

# This variable is created by user input for monthly utilities payment
utilities=float(input("What is your monthly utilities budget?: "))

# This variable is created by user input for monthly grocery budget
groceries=float(input("What is your monthly groceries budget?: "))

# This variable is created by user input for monthly transportation budget
transportation=float(input("What is your monthly transportation budget?: "))

# This variable is created by user input for monthly health care budget
health_care=float(input("What is your monthly health care budget?: "))

# This variable is created by user input for monthly personal care budget
personal_care=float(input("What is your monthly personal care budget?: "))

# This variable is created by user input for monthly clothing budget
clothing=float(input("What is your monthly clothing budget?: "))

# This variable is created by user input for monthly debt amount
debt=float(input("What is your monthly debt amount?: "))

# This variable is created to show monthly income leftover after expenses
savings=income-mortgage-utilities-groceries-transportation-health_care-personal_care-clothing-debt

# Once the input is received the below functions will...
# Calculate the percentage of the total budget spent in each category.

mortgage_percent=mortgage/income*100
utilities_percent=utilities/income*100
groceries_percent=groceries/income*100
transportation_percent=transportation/income*100
health_care_percent=health_care/income*100
personal_care_percent=personal_care/income*100
clothing_percent=clothing/income*100
debt_percent=debt/income*100

#Empty print to create space between input and outcome
print("")

# Output of calculated budget and resulting savings amount
print(f'Your monthly income is: ${income:.2f}')
print(f'Your monthly mortgage payment of ${mortgage:.2f} is {mortgage_percent}% of monthly income.')
print(f'Your monthly utilities payment of ${utilities:.2f} is {utilities_percent}% of monthly income.')
print(f'Your monthly groceries payment of ${groceries:.2f} is {groceries_percent}% of monthly income.')
print(f'Your monthly transportation payment of ${transportation:.2f} is {transportation_percent}% of monthly income.')
print(f'Your monthly mortgage payment of ${health_care:.2f} is {health_care_percent}% of monthly income.')
print(f'Your monthly mortgage payment of ${personal_care:.2f} is {personal_care_percent}% of monthly income.')
print(f'Your monthly mortgage payment of ${clothing:.2f} is {clothing_percent}% of monthly income.')
print(f'Your monthly mortgage payment of ${debt:.2f} is {debt_percent}% of monthly income.')

# If statements added to congratulate or scold you depending on how well you budgeted for the month.
# I realize we haven't learned this yet but I wanted to have fun with my program.
if savings>0:
    print(f'After expenses you have ${savings:.2f} leftover to add to your savings!')
if savings<0:
    print(f'Unfortunately after expenses you have ${savings:.2f} left that will need to be pulled from your savings.')
    print('\U0001F641')
