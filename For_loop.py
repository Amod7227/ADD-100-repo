# Program for finding #'s divisible by 7

#Creates list of #'s 1-300
for x in range(1,300,1):
    # If # in list is between 1 and 300 it checks to see if it's divisible by 7
    if( x%7 == 0):
        # If # is divisible by 7 it prints the #
        print(x)

