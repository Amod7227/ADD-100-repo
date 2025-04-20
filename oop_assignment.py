# Class definition for a Person
class Person:
    # Initializer with private variables
    def __init__(self, name, address, age, phone_number):
        self._name = name  # Private variable for name
        self._address = address    # Private variable for address
        self._age = age    # Private variable for age
        self._phone_number = phone_number # Private variable for phone number

    # Method to get student's info as a formatted string
    def get_data(self):
        return f"{self._name}, {self._address}, {self._age}, {self._phone_number}"

    # Getter for name
    def get_name(self):
        return self._name

    # Getter for address
    def get_address(self):
        return self._address

    # Getter for age
    def get_age(self):
        return self._age

    # Getter for phone number
    def get_phone_number(self):
        return self._phone_number

    # Setter for name
    def set_name(self, name):
        self._name = name

    # Setter for address
    def set_address(self, address):
        self._address = address

    # Setter for age
    def set_age(self, age):
        self._age = age

    # Setter for phone number
    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    # Instructions for displaying info of "persons"
    def display_data(self):
        print()
        print("Name:", self._name)
        print("Address:", self._address)
        print("Age:", self._age)
        print("Phone Number:", self._phone_number)
        print()


#program that creates three instances (objects) of the Person class
person_1= Person("John", "123 Sesame Street", 25, "1(800)123-4567")
person_2= Person("Jane", "1994 Ford Bronco Way", 66, "1(234)567-8910")
person_3= Person("Billy-Bob", "2001 A-Space-Odyssey Drive", 42, "1(234)867-5309")

#Display Data for created persons
print(person_1)
person_1.display_data()
print(person_2)
person_2.display_data()
print(person_3)
person_3.display_data()