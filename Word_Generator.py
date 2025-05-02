#Create an original list of 5 letters for the Program
Letter_List = ['a', 'e', 'i', 'o', 'u']



#Define a generator function two_letter_combinations
def two_letter_combinations(char_list):
    #Use nested loops within the generator function to iterate over the list of characters.
    #outer loop to produce first character
    for first_char in char_list:
        #Inner nested loop to produce second character of combination
        for second_char in char_list:
            #concatenate (Combine) the outcomes for the list and use yield to produce the results
            yield first_char + second_char





#Create main function
def Letter_Combo():
    #Throw-away Print function to explain what is being outputted by program
    print("Available combinations of the list of letters: a, e, i, o, & u")
    #for loop to iterated over the generator to print each combination of letters
    #Letter list inputted into generator 
    for list in two_letter_combinations(Letter_List):
        #print outcome of generator function
        print(list)

#call main function to run program
Letter_Combo()