def main():
# Example string
    example_string = "Hello, Python programmers!"
# Iterate through the string and print each character
    print("Iterating through the string:")
    for character in example_string:
        print(character)
# Find and print the character with the minimum ASCII value in the string
    min_ascii=min(example_string)
    print(f"\nCharacter with the minimum ASCII value:", "'",min_ascii, "'")
# Find and print the character with the maximum ASCII value in the string
    max_ascii=max(example_string)
    print("\nCharacter with the maximum ASCII value:", max_ascii)
# Find and print the index of the first occurrence of 'o' in the string
    first_o=example_string.find("o")
    print("\nIndex of 'o':", first_o)
# Convert the string into a list of characters and print the list
    print("\nConverting string to a list of characters:")
    string_list=list(example_string)
    print(string_list)
# Count and print the number of occurrences of 'o' in the string
    O_count=example_string.count("o")
    print("\nCount of 'o' in the string:", O_count)


main()
