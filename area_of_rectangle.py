class Rectangle:
    def get_measure(self):
        self.length = int(input("Enter the length of the rectangle: "))
        self.breadth = int(input("Enter the breadth of the rectangle: "))
    def area(self):
        print(f"area of rectangle is : {self.length * self.breadth}")
    def perimeter(self):
        print(f" The perimeter is : {2 * (self.length + self.breadth)}")
    def property(self):
        print(f"Rectangle has sum of all the sides is 360")

a1=Rectangle()
a1.get_measure()
a1.perimeter()
a1.area()
print(a1.property())