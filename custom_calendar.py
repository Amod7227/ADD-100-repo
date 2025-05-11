#imports calendar and datetime module
import calendar
import datetime

#main function for program
def custom_calendar():

    print("\n")
    #Added flare
    print("*-*-*-*-*-*-*-*-*")
    #current year via datetime module
    current_year = datetime.datetime.now().year

    #controls loop, ***Without while loop any wrong input will break the program. I've tried***
    loop_control = False

    #Initialized outside of while loop 
    user_birth_month = None

    #While loop to handle invalid user inputs
    while not loop_control:
        #try block to handle exceptions
        try:
            #ask user to input birth month
            user_birth_month = int(input("What Month were you born? (as a number. May would be 5):  "))
            #flare
            print("-*-*-*-*-*-*-*-*-")
            # If statement to ensure valid input is received
            if user_birth_month >= 1 and user_birth_month <= 12:
                #Loop control stops while loop if user inputs # 1-12
                loop_control = True 
                #Informs user of month selection
                print(f"User selected month {user_birth_month}")
                #flare
                print("*-*-*-*-*-*-*-*-*")
            
            #Else statement in event invalid user input is received
            else:
                print("Error: Input must be between 1 and 12.")
            
            
    
        #Except block to handle input errors
        except ValueError:
            #Print statement if error occurs
            print("Error: Input must be between 1 and 12.")
    
    #prints custom calendar
    print("Here is your custom calendar for your birth month this year:")
    #more flare
    print("-*-*-*-*-*-*-*-*-\n")
    print(calendar.month(current_year, user_birth_month))



#Call main function
custom_calendar()