#Hasattr function
def check_property(pet_obj):
    print("pet_name?", hasattr(pet_obj, "_vet_office__pet_name"))
    print("pet_id?", hasattr(pet_obj, "_vet_office__pet_id"))
    print("pet_type?", hasattr(pet_obj, "_vet_office__pet_type"))


#Class for vet system
class vet_office:
    #Class Variable
    Vet_name= "C.J.'s Vet"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="dog"):
        # Instance variables
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

        # Getter and Setters for pet variables
    def get_owner_first_name(self):
        return self.__owner_first_name
    
    def get_owner_last_name(self):
        return self.__owner_last_name
        
    def get_pet_id(self):
        return self.__pet_id
    
    def get_pet_name(self):
        return self.__pet_name
    
    def get_pet_type(self):
        return self.__pet_type

    def set_owner_first_name(self, value):
        self.__owner_first_name = value
    
    def set_owner_last_name(self, value):
        self.__owner_last_name = value

    def set_pet_id(self, value):
        self.__pet_id = value
    
    def set_pet_name(self, value):
        self.__pet_name = value
    
    def set_pet_type(self, value):
        self.__pet_type = value

    #Instructions for displaying info of "persons"
    def display_data(self):
        print()
        print("First:", self.__owner_first_name)
        print("Last:", self.__owner_last_name)
        print("Pet ID:", self.__pet_id)
        print("Patient Name:", self.__pet_name)
        print("Pet Type: ", self.__pet_type)
        print()







#create three instances (objects) of the Pet class
pet_1= vet_office("John", "Doe", 8675309, "Bo")
pet_2= vet_office("Jane", "Deer", 1234567, "Rex")
pet_3= vet_office("Billy-Bob", "Thornton", 1001010, "Pistachio")


#Show setter method for one object
pet_1.set_pet_name("Ignatius")

#Display Data for created persons
print(vet_office.Vet_name, "offices patients:")
#print(pet_1)
pet_1.display_data()
#print(pet_2)
pet_2.display_data()
#print(pet_3)
pet_3.display_data()

print("Patient 1")
check_property(pet_1)
print("Patient 2")
check_property(pet_2)
print("Patient 3")
check_property(pet_3)
