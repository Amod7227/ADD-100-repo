# Grading program
user_grade=int(input("What is your numeric grade?: "))

# Output for letter grade
#Check if grade is less than 60
if user_grade < 60:
    print("Your letter grade is: F")
#Check if grade is less than 70
elif user_grade <= 69:
    print("Your letter grade is: D")
#Check if grade is less than 80
elif user_grade <= 79:
    print("Your letter grade is: C")
#check if grade is less than 90
elif user_grade <= 89:
    print("Your letter grade is: B")
#check if grade is 90 or above
else:
    print("Your letter grade is: A")