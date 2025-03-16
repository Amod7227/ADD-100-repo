
# List of seats
available_seats=list(range(1,21))

# Empty list for taken seats
taken_seats=[]

# Empty list for customers
customer=[]

# Input of customer name
customer=(input("Hello. What is the name for the reservation?: "))
# List of Currently available seats and customer input to select a seat
print("Current available seats are: ", available_seats)
print("To end your purchase enter 0")
seat_to_move = int(input("Enter the seat you would like to reserve: "))


# Function to select seat and remove it from available list
def reserve_seat():
    if seat_to_move in available_seats:
        available_seats.remove(seat_to_move)
        taken_seats.append(seat_to_move)
        print(f"Moved '{seat_to_move}' to the reserved list.")
        print("Available seats:", available_seats)
# Error messages if seat unavailable
    elif ValueError:
        print("Please enter the seat number you would like.")

    else:
        print(f"Error: Seat '{seat_to_move}' not found in the available list of seats.")

# Calls function after input is entered
reserve_seat()

# While loop to allow for more seat reservations
while seat_to_move != 0:
    seat_to_move = int(input("\nAre there any other seats you would like to reserve?: "))
    reserve_seat()


# If input is 0 cancels program
if seat_to_move == 0:
    print("\nThank you", customer, "for your reservations.")
    print("You have reserved seats:", taken_seats)
    print("Please come again!")


# List of seats
available_seats=list(range(1,21))

# Empty list for taken seats
taken_seats=[]

# Empty list for customers
customer=[]