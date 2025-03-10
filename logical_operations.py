# Logical operations program

# User input for program
num1 = int(input("Enter an integer.: "))
num2 = int(input("Enter another integer.: "))

# Empty print to separate output
print("")
# And logical operation
print("Both numbers are greater than 0: ", num1>0 and num2>0)
# Empty print to separate output
print("")
# And logical operation
print("Both Numbers are less than or equal to 100: ", 100>=num1 and 100>=num2)
# Empty print to separate output
print("")
# Or logical operation
print("One number is greater than 100: ", num1>100 or num2>100)
# Empty print to separate output
print("")
# Or logical operation
print("One number is even: ", num1%2==0 or num2%2 == 0)
# Empty print to separate output
print("")
# Not logical operation
if not num1 == num2:
    print("Number 1 is not equal to Number 2: ", num1!=num2)
else:
    print("Number 1 is equal to number 2: ", num1==num2)
# Empty print to separate output
print("")
# Not logical operation
if not num2>num1:
    print("Number 2 is not greater than Number 1: ", num2<num1)
else:
    print("Number 2 is greater than Number 1: ", num2>num1)