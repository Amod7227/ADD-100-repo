#Input Madlib for song
input_verb = input("Enter a verb: ")
input_adjective = input("Enter an adjective with the suffix 'ness' (ie. bitterness): ")
input_verb2 = input("Enter a plural verb: ")
input_verb3 = input("Enter another plural verb: ")
input_noun1 = input("Enter a noun: ")
input_pronoun1 = input("Enter a pronoun: ")
input_adverb = input("Enter an adverb: ")
input_adverb2 = input("Enter an adverb: ")
input_verb4 = input("Enter another verb: ")
input_object1 = input("Enter an object: ")
input_direction = input("Enter a direction: ")
input_verb5 = input("Enter another verb: ")
input_verb6 = input("Enter another verb: ")
input_verb7 = input("Enter another verb: ")
input_time_of_day = input("Enter a time of day 'morning, evening etc.': ")



# Song function
def song(verb, adjective, verb2, verb3, noun1, pronoun, adverb, adverb2, verb4, verb5, verb6, verb7, object1, direction, time_of_day,):
    print("\n\n")
    print(f"Step one, you say we need to {verb}")
    print(f"He {verb2}, you say sit down, it's just a {verb}")
    print(f"He {verb3} {adverb} back at you")
    print(f"You {verb4} {adverb} right on through")
    print(f"Some sort of {object1} to your right")
    print(f"As he goes {direction}, and you stay right")
    print(f"Between the lines of {verb5} and {verb6}")
    print(f"You begin to wonder why you {verb7}")
    print()
    print(f"Where did I go wrong?")
    print(f"I lost a {noun1}")
    print(f"{adverb2} along in the {adjective}")
    print(f"And I would have stayed up with {pronoun} all {time_of_day}")
    print(f"Had I known how to save a {noun1}")

#song output
song(verb=input_verb, adjective=input_adjective, verb2=input_verb2, verb3=input_verb3, noun1=input_noun1, pronoun=input_pronoun1, adverb=input_adverb, adverb2=input_adverb2, verb4=input_verb4, object1=input_object1, verb5=input_verb5, verb6=input_verb6, verb7=input_verb7, direction=input_direction, time_of_day=input_time_of_day )