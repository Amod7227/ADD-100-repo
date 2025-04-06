# Dictionary of Nato Alphabet
NATO_Alphabet = { 'a' : 'Alpha', 'b': 'Bravo', 'c': 'Charlie', 'd': 'Delta', 'e': 'Echo',  'f': 'Foxtrot', 'g': 'Golf', 'h': 'Hotel','i': 'India','j': 'Juliet','k': 'Kilo','l': 'Lima','m': 'Mike','n': 'November','o': 'Oscar','p': 'Papa','q': 'Quebec','r': 'Romeo','s': 'Sierra','t': 'Tango','u': 'Uniform','v': 'Victor','w': 'Whiskey','x': 'X-Ray','y': 'Yankee','z': 'Zulu'}

# Spelling Program to decipher inputted word and pull dictionary equivalent
def spelling_program(word):
    #translates letter to lowercase to match dictionary key's
    for letter in word.lower():
        if letter in NATO_Alphabet:
            #Prints value based off key pair entry from input
            print(f"{NATO_Alphabet[letter]}")

# Main function for input
def translation():
    words = input("Please enter a word to see it's Nato spelling:")
    spelling_program(words)

#calls function to run
translation()