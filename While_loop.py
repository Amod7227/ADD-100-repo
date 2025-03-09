# 99 Bottles of beer on the wall song

# Input function to create variable for # of bottles of beer song starts at 
drinks = int(input("How many bottles of beer do we have?: "))
print(" ")

# Bottle vs Bottles dictionary
# Creates variables for, b= '#' of bottles, objects = bottles, transition = the changed version of bottle(s)
def song(b):
    if (b==1):
        objects = 'Bottle'
        transition = 'Bottles'
    elif (b==2 ):
        objects = 'Bottles'
        transition = 'Bottle'
    else:
        objects = 'Bottles'
        transition = 'Bottles'

# Print statements for singing the song and reducing '#' of bottles by 1
    if (b>0):
        print(str(b)+ " " + objects + " of beer on the wall, " + str(b) + " " + objects + " of beer.")
        print("Take one down and pass it around, " + str(b-1) + " " + transition + " of beer on the wall.")
        # Transition space between next line of song
        print("")
    elif (b==0):
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, we need 99 more bottles of beer on the wall.")
    else:
        print('"Where did the rum go", Captain Jack Sparrow')

# '#' of bottles begins at 99
Bottles = drinks

# While loop for 99 bottles song
while Bottles >= 0:
    song(Bottles)
    Bottles -= 1