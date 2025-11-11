"""Create the Pet Class:
Define a Pet class with attributes: kind (e.g., dog, cat), breed, and name.
Implement get and set methods for each of these attributes.
Add a method called print_details that prints the details of the pet.
Create Instances:
Create three objects of the Pet class with different kinds, breeds, and names.

Call the print_details method for each object that you created

Demonstrate a Special Method or Function:
Choose three of the following and demonstrate its use with the Pet class instances:

__name__: Display the name of the class.
type(): Show the class used to instantiate a pet object.
__module__: Return the module name in which the Pet class is defined.
__bases__: Display the base classes of the Pet class (if any).
isinstance(): Check if an instance is of the Pet class.
"""
class pet:

    vet_office = "Clifford"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type = "dog"):
        # Instance variables
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

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

    def print_student_details(self):
        print("display dog details: ", vars(self))
    
    def print_info(self):
        print(self.__owner_first_name)
        print(self.__owner_last_name)
        print(self.__pet_id)
        print(self.__pet_name)
        print(self.__pet_type)

def main():
    
    pet1 = pet("John", "Deven", "123456", "henry", "shetzu")
    pet2 = pet("serge", "Smith", "789012", "fred", "poodle")
    pet3 = pet("ivan", "andrew", "475612", "tiger", "multece")

    print(pet1.get_owner_first_name())
    print(pet1.get_owner_last_name())
    print(pet1.get_pet_id())
    print(pet1.get_pet_name())
    print(pet1.get_pet_type())

    print(pet2.get_owner_first_name())
    print(pet2.get_owner_last_name())
    print(pet2.get_pet_id())
    print(pet2.get_pet_name())
    print(pet2.get_pet_type())
     
    print(pet3.get_owner_first_name())
    print(pet3.get_owner_last_name())
    print(pet3.get_pet_id())
    print(pet3.get_pet_name())
    print(pet3.get_pet_type())

    pets = pet("pet last name", "pet last name", "pet id", "pet name", "pet type")
    print(hasattr(pets, "_owner__first_name"))
    print(hasattr(pets, "_owner__last_name"))
    print(hasattr(pets, "_pet_id"))
    print(hasattr(pets, "_pet_name"))
    print(hasattr(pets, "_pet_type"))

    print("now testing setters")

    pet1.set_owner_first_name("hammer")
    pet1.set_owner_last_name("nail")
    pet1.set_pet_id("217384")
    pet1.set_pet_name("snail")
    pet1.set_pet_type("luandrei")

    pet2.set_owner_first_name("hamster")
    pet2.set_owner_last_name("hammer")
    pet2.set_pet_id("456384")
    pet2.set_pet_name("nail")
    pet2.set_pet_type("huskie")

    pet3.set_owner_first_name("ham")
    pet3.set_owner_last_name("snicker")
    pet3.set_pet_id("217395")
    pet3.set_pet_name("hamster")
    pet3.set_pet_type("poodle")

    print(pet1.get_owner_first_name())
    print(pet1.get_owner_last_name())
    print(pet1.get_pet_id())
    print(pet1.get_pet_name())
    print(pet1.get_pet_type())

    print(pet2.get_owner_first_name())
    print(pet2.get_owner_last_name())
    print(pet2.get_pet_id())
    print(pet2.get_pet_name())
    print(pet2.get_pet_type())

    print(pet3.get_owner_first_name())
    print(pet3.get_owner_last_name())
    print(pet3.get_pet_id())
    print(pet3.get_pet_name())
    print(pet3.get_pet_type())


main()