
def main_menu():
        print("Menu:")
        while True:
            try:
                print("\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries.\n")
                print("1. Create a new entry")
                print("2. Display an entry by last name")
                print("3. Update an existing entry")
                print("4. Remove an entry")
                #Added option to view entire list of entries, not ideal for customers
                #in a real life application but I wanted to try it out
                print("5. View entire list of entries")
                print("6. Quit application")
                choice = int(input("Please enter the number of your selection: "))
                #Choices changed to 6 for extra function added
                if 1 <= choice <= 6:
                    return choice
                else:
                    print("That is not a valid number. Try again.")
            except ValueError:
                print("That is not a valid number. Try again.")

def main():
    choice = 0
    #Choices changed to 6 for extra function added
    while choice != 6:
        choice = main_menu()
        if choice == 1:
            create()
        elif choice == 2:
            read()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        #Added function to list entries
        elif choice == 5:
            listing()
    print("\nData saved as customer_list.txt\n")

def check():
        try:
            file = open("customer_list.txt", 'r')
            lines = file.readlines()
            file.close()
            return lines
        except FileNotFoundError:
            print("Customer list does not exist. Creating a new file...")
            return []

def create():
    customer = check()
    fname = input("Please enter the customer's first name: ")
    lname = input("Please enter the customer's last name: ")
    phone = input("Please enter the customer's phone: ")
    email = input("Please enter the customer's email: ")
    entry = f"{fname}, {lname}, {phone}, {email}\n"
    customer.append(entry)
    save(customer)

def save(output):
    file = open("customer_list.txt", 'w')
    for line in output:
        file.write(line)
    file.close()
    print("File updated.")

def read():
    customer = check()
    #If not customer to run if no entries in txt file
    if not customer:
        #print statement if no entries in txt file
        print("No data to display")
        return
    #user input for search by last name
    last_name = input("What is the last name of the entry you'd like to locate?: ")
    #flag set to false outside of for loop
    found = False
    for line_item in customer:
        if line_item.strip() == "":
            continue
        #variable to pull from customer and add commas between inputs from txt entries
        data = line_item.strip().split(", ")
        #Checks the entries for the second position to verify lname input
        if len(data) == 4 and data[1].lower() == last_name.lower():
            #print statement for found customer in .txt file
            print(f"Customer found: {line_item.strip()}")
            #flag changed to true if customer found
            found = True
    
    if not found:
        #print statement if no match found in .txt file
        print("\nNo data matching that request\n")

def update():
    customer = check()
    if not customer:
        print("\nNo entries to update.\n")
        return
    #Input to find data entry to change based on customer last name
    last_name = input("\nWhat is the last name of the entry you'd like to update?: \n")
    #update flag set to false outside of for loop
    updated = False
    #empty list created to save new input
    changes = []
    #for loop to update information for customers via person variable
    for person in customer:
        if person.strip() == "":
            continue
        data = person.strip().split(", ")
        if len(data) == 4 and data[1].lower() == last_name.lower():
            print(f"Current customer data: {person.strip()}")
            #Input for new phone number
            updated_phone_number = input("Enter the new phone number for this customer\n(please leave entry blank to keep current Phone number): ")
            #input for new email
            updated_email = input("Enter new email address for this customer\n(please leave entry blank to keep current Email): ")
            #if phone number is updated this block executes
            if updated_phone_number:
                #3rd item in list which is the phone number gets changed to updated variable
                data[2] = updated_phone_number
            #if email updated this block executes
            if updated_email:
                #the 4th item in the list gets changed to the updated variable
                data[3] = updated_email
            #variable for new data that will be appended to txt file
            updated_entry = ", ".join(data) + "\n"
            #appends new list to txt file
            changes.append(updated_entry)
            #updated flag set to true upon update being made
            updated = True
        else:
            changes.append(person)
    # if block dependant on true/false updated flag
    if updated:
        save(changes)
        print("\nCustomer information has been updated.\n")
    else:
        print("\nNo matching customer found.\n")

def delete():
    customer = check()
    if not customer:
        print("\nNo entries to delete.\n")
        return
    #variable created to hold user input for customer that will be deleted
    customer_to_delete = input("Enter the last name of the customer to delete: ")
    #empty list generated outside for loop to hold deletion data
    deletions = []
    #flag set to false outside of loop
    deleted = False
    #for loop to remove users via removed_user variable
    for removed_user in customer:
        if removed_user.strip() == "":
            continue
        data = removed_user.strip().split(", ")
        if len(data) == 4 and data[1].lower() == customer_to_delete.lower():
            #Print statement describing which customer is being deleted from database
            print(f"Deleting customer: {removed_user.strip()}")
            #Flag set to true after deletions were made
            deleted = True
            continue  # Skip this line (i.e., delete it)
        deletions.append(removed_user)
    #if block dependent on true/false deleted flag
    if deleted:
        save(deletions)
        print("Customer information deleted.")
    else:
        print("No matching customer found.")

#Added function to list entries
def listing():
    customer = check()
    print("\nList of customers in DataBase: \n")
    #enumerate adds numbers to list for ease of viewing
    for i, entry in enumerate(customer, start=1):
        if entry.strip() == "":
            continue
        #prints enumerated list of entries: the more the merrier!
        print(f"{i}. {entry.strip()}")
    



#Call main function to run
main()