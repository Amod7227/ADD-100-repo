#class for pets
class pet:
    pet_class_name= "The Wonder Pets"

    def __init__(self, pet_type, pet_breed, pet_name):
        # Instance variables
        self.pet_breed = pet_breed
        self.pet_name = pet_name
        self.pet_type = pet_type

    # Getter and Setters for pet variables        
    def get_pet_breed(self):
        return self.pet_breed
    
    def get_pet_name(self):
        return self.pet_name
    
    def get_pet_type(self):
        return self.pet_type

    def set_pet_breed(self, value):
        self.pet_breed = value
    
    def set_pet_name(self, value):
        self.pet_name = value
    
    def set_pet_type(self, value):
        self.pet_type = value
    
    
    #Add a method called print_details that prints the details of the class pet.
    def print_details(self):
        print("-*-*-*-*-")
        print("Pet Type:", self.pet_type)
        print("Pet Breed:", self.pet_breed)
        print("Pet Name: ", self.pet_name)
        print("-*-*-*-*-")


# 3 created pets of the "Wonder Pets"
pet_1=pet("Duck", "Rouen Duck", "Ming-ming Duckling")
pet_2=pet("Turtle", "Painted Turtle", "Tuck")
pet_3=pet("Guinea pig", "American Guinea Pig", "Linny")



#class name
print(pet.pet_class_name)
#Call method print_details to print details of pets
pet_1.print_details()
pet_2.print_details()
pet_3.print_details()


# Choose three of the following and demonstrate its use with the Pet class instances:

#getattr(): Use it to access an attribute of a Pet instance.
print("pet_1 name:", getattr(pet_1, 'pet_breed'))
#type(): Show the class used to instantiate a pet object.
print("pet_2 class:", type(pet_2))
#isinstance(): Check if an instance is of the Pet class.
print("pet_3 is a member of the Wonder Pets: ", isinstance(pet_3, pet))