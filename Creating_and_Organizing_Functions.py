#

# Factorial function with recursive elif step and prompt for positive integer
def factorial(n):
    if n == 0 or n ==1:
        return 1
    elif n>1:
        return n * (factorial (n - 1))
    #Prompt for new number if integer is negative
    else:
        print("Please try again with a non-negative number.")

# Input for number to test
number=int(input("Please enter a number to determine its factorial.: "))

# Variable created from factorial function
answer = factorial(number)

# Outputted value of factorial if positive integer is inputted
if number >= 0:
    print(f"The result for the number {number} is {answer}.")