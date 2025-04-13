#Empty list to hold books for program
books = []

#Main function for program
def book_titles():
    print("Please enter a total of 10 book titles for your list")
    #While loop to gather books until 10 books are inputted
    while len(books) <10:
        #Input for books
        book_title=input("Please enter book title: ")
        #Capitalizes book titles and adds them to books list
        books.append(book_title.title())
    #new variable that sorts the books into alphabetical order
    books_sorted = sorted(books)

#Prints list of books in alphabetical order with for loop to iterate each entry from the list
    print("Your books:")
    for book in books_sorted:
        print(book)


#Calls book_titles function to run
book_titles()