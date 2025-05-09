# calculate a person's age in: Years, months, weeks, days
# 30.41 days in a month
# 7 days in a week 

from datetime import datetime

#Main function
def main():
   
   #prints new line for output
    print("\n\n")
    #try block to handle exceptions
    try:
        #Creates today variable with datetime
        today = datetime.today()
        #Ask user to input birth year
        birth_year = int(input("What year were you born?  "))
        #ask user to input birth month
        month = int(input("What Month were you born (as a number. May would be 5)  "))
        #ask user to input birth day
        day = int(input("What day of the month were you born?  "))
        # just need datetime not datetime.date
        # because we imported datetime from datetime
        #Users birthday based on input above
        birthday = datetime(birth_year, month, day)
        #Print statement to provide birthday
        print("Your birthday is: ")
        #Formats birthday in year month day format
        birthday_output = birthday.strftime("%Y-%m-%d")
        #Prints birthday from inputted variables
        print(birthday_output) 

        #Variable created to subtract birthday from todays date
        delta = today - birthday
        #print statement to show the difference in days from birthday to today
        print(f'Difference is {delta.days} days')
        #Variable created to show how old you are based on delta variable
        delta_years = delta.days // 365.2425
        
        #Variable to find exact years old
        exact_years= delta.days / 365.2425

        #variable created to show months
        echo = exact_years * 12

        #Variable created to show weeks by multiplying years by weeks in 4 years divided by 4(to include leap years)
        foxtrot = exact_years * 52.17875

        #variable to show age in hours
        golf = delta.days * 24

        #Variable to show age in minutes
        hotel = golf * 60

       #print statement to show how old user is based on user input
        print(f'You are {delta_years} years old')
        print(f"Which is {echo:.2f} months old")
        print(f"Or {foxtrot:.2f} weeks old")
        print(f"Or {golf} hours old")
        print(f"Or {hotel} minutes old")
      #Exception block to handle unexpected errors
    except Exception as e:
        #Print statement if error occurs
        print(f"ooooops!!!:  {e}") 
        #Calls main function in case of error
        main()
#Calls main function
main()