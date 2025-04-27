#New custom exception class
class not_numeric_error(Exception):
    print("InvalidInputError")
    pass



#Main function to Write a Python script that prompts the user to input a number.
def main():
    try:
    #try block for user input that may trigger custom exception
        User_input=(input("Please enter a number: "))
        if User_input.isnumeric():
            pass
        if not User_input.isnumeric():
            raise not_numeric_error
            
    except not_numeric_error as e:
    # Code that runs if an exception occurs
        print(f"An error occurred: {e}")
        print("You're a moron that didn't enter a number as instructed!")
        main()
    else:
    #Code that runs if user enters a number and doesn't break the program
        print("Congrats! You are a genius and entered a number!")
    
    finally:
        print("* If you see this message more than once, Public schools failed you.\nThanks for running this useless program! Please come again!")



#Calls main program to run
main()