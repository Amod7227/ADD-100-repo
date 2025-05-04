#Main function: sales_list to import file from sales_totals.txt
def sales_list():
    #try block to handle errors
    try:
        print("Salesman Sales List:")
        #initialize total_sales and sales_count variables for use within the loop
        total_sales = 0.0
        sales_count = 0

        # creates file path due to ADD issue
        file_path='ADD-100-repo/sales_totals.txt'
        #Opens sales_totals.txt file in read format
        with open(file_path, 'r') as file:
            line = file.readline()
            #Add each number from individual line to running total within loop
            while line:
                #.strip removes newline and whitespace per instructions
                line = line.strip()
                #new try block within loop to handle exceptions
                try:
                    #Converts line from .txt file to float
                    number = float(line)
                    #Converts and prints line from txt file to currency format
                    #\n separates lines for readability
                    #sales_count added to show which number of sale each line is
                    print(f"\n{sales_count+1}) ${number:,.2f}")
                    #Creates running total from float numbers above
                    total_sales += number
                    #Totals count of individual lines added to total
                    sales_count += 1
                     #Average created from total and count
                    average_value = total_sales/sales_count
                #new except block within loop to handle inside loop exceptions
                except Exception:
                    print("A error has occurred.")
                #reads file line by line
                line = file.readline()


        #Dollars needed for presidents club or million dollar club
        presidents_club=1000000-total_sales

        #Displays sales summary from data within loop
        print("")#Creates new line between list and sales totals below for ease of viewing
        print("Individual Sales Totals for year:")
        print(f"Total Value of sales: ${total_sales:,.2f}") #total sales taken from inside loop above
        print(f"Individual sales count: {sales_count}") #Count taken from inside loop above
        print(f"Average sale value: ${average_value:,.2f}") #average taken from inside loop above
        print(f"Total sales amount needed for Presidents Club status: ${presidents_club:,.2f}")
    #Except block to handle errors
    except Exception:
        print("An Error has occurred.")


#Call main function
sales_list()