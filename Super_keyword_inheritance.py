#Super key word is used to refer the parent class
# class A:
#     def show(self):
#         print("Hello")
#
# class B(A):
#     def show(self):
#         print("Hai")
#
# s1 = B()
# s1.show()
class veihcle:
    def __init__(self, brand, fuel_type):
        self.brand = brand
        self.fuel_type = fuel_type

    def display(self):
        print(f"Brand : {self.brand}")
        print(f"Fuel_type : {self.fuel_type}")

class Car(veihcle):
    def __init__(self,brand,fuel_type,model):
        super().__init__(brand,fuel_type)
        self.model = model
    def display_details(self):
        self.display()
        print(f"Model is : {self.model}")
c = Car("Toyota", "Petrol", "camry")
c.display_details()

