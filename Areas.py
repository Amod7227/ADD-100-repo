#Variable for pi
pi=3.14159265

# Defined functions for square
def square(square_area):
    return side*side
    
#Defined function for circle
def circle(circle_area):
    return pi * radius * radius

# Input for length of side
side = int((input("What is the length of your square's side?: ")))
#input for Square units
square_units = (input("What unit are you measuring your side in?: "))
# Input for length of radius
radius = (int(input("What is the radius of your circle?: ")))
#input for radius units
radius_units = (input("What unit are you measuring your radius in?: "))
# Calls function and delivers output of area for square
print(f"The area of your square is {square(side):.2f} square {square_units}.")
# Calls function and delivers output for area of circle
print(f"The area of your circle is {circle(radius):.2f} square {radius_units}.")