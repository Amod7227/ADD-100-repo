# Inputs for height and weight
pounds= int(input("What is your weight in pounds?: "))
inches= int(input("What is your height in inches?: "))


# Global variables
global KG
KG= pounds * .453592
global meters
meters= inches * .0254

# Function to calculate BMI based off of Communist unit of measurement
def calculate_bmi(KG, meters):
    BMI= KG / (meters * meters)
    return BMI

# Output of BMI
BMI= calculate_bmi(KG, meters)
print()
print(f"Based on your height of {inches} inches \nand weight of {pounds} pounds. \nYour BMI is {BMI:.2f}.")

# If, elif, else to determine weight category
if BMI <= 18.5:
    print("You are in the underweight category.")
elif BMI <= 24.9:
    print("You are in the normal weight category.")
elif BMI <=29.9:
    print("You are in the over weight category.")
else:
    print("You are in the obese category.")

# My thoughts on BMI as a measurement
print("But don't worry what category you fall in.\nBmi is a poor metric to test a persons physical fitness.")