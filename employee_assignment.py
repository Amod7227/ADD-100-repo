#Assignment part 1: Create class and subclass for employee program
#Employee class
class employee:
    Company_name= "Bob's Warehouse"
    #Employee is the superclass for production worker class
    def __init__(self, employee_name, employee_number):
        self._employee_name=employee_name
        self._employee_number=employee_number

    #Getters
    def get_employee_name(self):
        return self._employee_name
    
    def get_employee_number(self):
        return self._employee_number
    
    #Setters
    def set_employee_name(self, value):
        self._employee_name= value

    def set_employee_number(self, value):
        self._employee_number= value


#sub class for employee titled production worker
class production_worker(employee):
    def __init__(self, employee_name, employee_number, shift_number, hourly_pay):
        #Variables from employee class
        super().__init__(employee_name, employee_number)
        #Sub class variables 
        self._shift_number = shift_number
        self._hourly_pay = hourly_pay

    #Getter for subclass
    def get_shift_number(self):
        return self._shift_number
    
    def get_hourly_pay(self):
        return self._hourly_pay
    
    #Setter for subclass
    def set_shift_number(self, value):
        self._shift_number=value

    def set_hourly_pay(self, value):
        self._hourly_pay=value


#Assignment part 2: write a script for implementing and testing
#Main function to input variables for employee data
def main():
    #Input for employee information 
    employee_name = input("Please enter workers name: ")
    employee_number = input("Please enter workers I.D. number: ")
    shift_number = int(input("Please enter workers shift number (1 or 2): "))
    hourly_pay = float(input("Please enter workers projected hourly pay: "))

    #Create an instance of ProductionWorker.
    ProductionWorker=production_worker(employee_name, employee_number, shift_number, hourly_pay)

    #store data with setter for display
    ProductionWorker.set_employee_name(employee_name)
    ProductionWorker.set_employee_number(employee_number)
    ProductionWorker.set_shift_number(shift_number)
    ProductionWorker.set_hourly_pay(hourly_pay)

    #Display employee information with the getter once received
    print("")
    print("")
    print("Employee info for", employee.Company_name)
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print("Employee Name: ", ProductionWorker.get_employee_name())
    print("Employee I.D. Number: ", ProductionWorker.get_employee_number())
    print("Employee's Shift: ", ProductionWorker.get_shift_number())
    print(f"Employee Hourly Pay: ${ProductionWorker.get_hourly_pay():.2f}")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print("")
    print("")



#Call main function to run program for employee information
main()