#

#Main function for program
def password_validator():
    #Try block to handle exceptions
    try:
         #While loop to run through password requirements
         while True:
        #input variable from user to gather a password
            print("Password must contain at least one uppercase letter.\nPassword must contain at least one lowercase letter.\nPassword must contain at least one number.\nPassword must contain at least one symbol from set: !@#$%&*':;><.,-_=+?/|.")
            initial_password = input("Enter a password: ")

        #ensures length of password is between 8 and 20 characters
            #Breaks function if not between 8 and 20
            if len(initial_password) < 8 or len(initial_password) > 20:
                print("Try again!\nPassword must contain at least one uppercase letter.\nPassword must contain at least one lowercase letter.\nPassword must contain at least one number.\nPassword must contain at least one symbol from set: !@#$%&*':;><.,-_=+?/|.")
                break
            elif len(initial_password) >=8 and len(initial_password)<=20:
                continue

        #flags for each requirement that is needed
            uppercase = False
            lowercase = False
            number = False
            symbol = False

        #for loop to check characters for required fields
            for char in initial_password:
                if char.isupper():
                    uppercase = True
                elif char.islower():
                    lowercase = True
                elif char.isdigit():
                    number = True
                elif char in "!@#$%&*':;><.,-_=+?/|":
                    symbol = True

        # Check to determine if all required fields are met
            if not (uppercase and lowercase and number and symbol):
                print("Try again!\nPassword must contain at least one uppercase letter.\nOne lowercase letter.\nOne number.\nOne symbol from set: !@#$%&*':;><.,-_=+?/|.")
                break

        #input variable to confirm password
            confirm_password = input("Please type password again to confirm your password: ")

        #Check to ensure both passwords match
            if initial_password == confirm_password:
                print("Password Successful")
                #Ends function if passwords match with successful message
                break  
            #else block if passwords don't match
            else:
                print("Password unsuccessful. Please try again.")
    #Exception block to handle exceptions
    except Exception:
        print("Exception occurred")

#calls function to run password_validator
password_validator()