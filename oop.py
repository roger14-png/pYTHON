# Assignment 1: Smartphone Class with Inheritance & Encapsulation

# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model}"


# Child Class (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)  # Inherit brand & model
        self.os = os
        self.__storage = storage  # Encapsulation: private attribute
    
    # Getter method
    def get_storage(self):
        return self.__storage
    
    # Setter method
    def upgrade_storage(self, extra_space):
        if extra_space > 0:
            self.__storage += extra_space
        else:
            print("Storage upgrade must be positive!")
    
    def call(self, contact):
        return f"📞 Calling {contact} from {self.brand} {self.model}..."


# Activity 2: Polymorphism Challenge
class Car:
    def move(self):
        return "Driving 🚗"

class Plane:
    def move(self):
        return "Flying ✈️"

class Boat:
    def move(self):
        return "Sailing 🚤"


# -------------------------
# MAIN PROGRAM (Demo)
# -------------------------
if __name__ == "__main__":
    print("=== Assignment 1: Smartphone Class ===")
    phone1 = Smartphone("Apple", "iPhone 14", "iOS", 128)
    print(phone1.info())
    print("Storage:", phone1.get_storage(), "GB")

    phone1.upgrade_storage(64)
    print("After upgrade:", phone1.get_storage(), "GB")

    print(phone1.call("Alice"))

    print("\n=== Activity 2: Polymorphism Challenge ===")
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        print(v.move())
