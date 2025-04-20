# Starting program 
def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    try:
        new_art_index = int(input("Enter the index of the artist you wish to replace: "))
        new_input=str(input("Enter the new artist to add to the top artists list: "))

        if new_art_index <= len(top_artists):
            top_artists[new_art_index] = new_input
        else:
            print("Invalid operation")
        print(top_artists)

    except (ValueError, IndexError) as e:
        print(f"An error occurred: {e}")

    except:
        print("Oops... Something went wrong.")



main()