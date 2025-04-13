# Import of "random" to allow for random integer to be produced
import random

# Main function for guessing game
def guessing_game():
    #Random int used to produce random integer between 0 and 1000
    magic_number= random.randint(0, 1000)
    
    #while loop to continue guessing game until answer is found
    while True:
        try:
            # User input for guessing game
            user_guess=  int(input("Try to guess the 'magic' number between 0 and 1000:"))
            #abs function to determine difference in guess and magic number
            incorrect_guess = abs(magic_number - user_guess)
        
            #Conditions for while loop to break or continue
            if user_guess == magic_number:
                print("Congrats, you nailed it!")
                break
            elif incorrect_guess <=5:
                print("Your guess was very hot, try again!")
            elif incorrect_guess <=25:
                print("Your guess was hot, try again!")
            elif incorrect_guess <=50:
                print("Your guess was warm, try again!")
            elif incorrect_guess <=100:
                print("Your guess was cold, try again!!!")
            elif incorrect_guess <=150:
                print("Your guess was very cold, try again!")
            else:
                print("Your guess was freezing, try again!")
        #Exception block to prevent user from inputting incorrect character type
        except ValueError:
            print("Please enter a number between 0 and 1000 and try again.")

# Called function to begin guessing game
guessing_game()