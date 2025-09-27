# -------------------------------
# Assignment 1: Design Your Own Class
# -------------------------------

# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"


# Child Class (Inheritance from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)   # call parent constructor
        self.storage = storage
        self.__battery = battery   # encapsulation (hidden attribute)

    def charge(self, amount):
        self.__battery += amount
        if self.__battery > 100:
            self.__battery = 100
        print(f"Battery charged to {self.__battery}%")

    def use(self, hours):
        self.__battery -= hours * 10
        if self.__battery < 0:
            self.__battery = 0
        print(f"After using {hours}h, battery is {self.__battery}%")

    def get_battery(self):
        return self.__battery


# Testing Assignment 1
print("=== Assignment 1: Smartphone Class ===")
phone1 = Smartphone("Samsung", "S22", "256GB", 80)
phone2 = Smartphone("Apple", "iPhone 14", "128GB", 50)

print(phone1.device_info())    # Samsung S22
print(phone2.device_info())    # Apple iPhone 14

phone1.use(2)                  # Decrease battery
phone1.charge(30)              # Recharge battery
print("Battery status:", phone1.get_battery())


# -------------------------------
# Activity 2: Polymorphism Challenge
# -------------------------------

class Vehicle:
    def move(self):
        print("The vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Testing Activity 2
print("\n=== Activity 2: Polymorphism Challenge ===")
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
