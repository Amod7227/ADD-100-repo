# Import random for guessing game
import random


#Main function for program
def main():
    random_number=random.randint(0,10)
    #While loop to keep game running
    while True:
        #try block 
        try :
             Guess = int(input("Guess a number between 0 and 10: "))
             print(random_number)
             if Guess == random_number:
                print("Congrats you guessed the number")
                break
             else:
                print("Incorrect guess.")
                Guess = int(input("Guess a number between 0 and 10: "))
        #Zero division exception block which theoretically should never be encountered
        except ZeroDivisionError:
            print("I don't know how you did it but you managed to divide by zero.")
        #Value error exception block 
        except ValueError:
            print("please enter a valid number between 0 and 10")

#call main function to run
main()