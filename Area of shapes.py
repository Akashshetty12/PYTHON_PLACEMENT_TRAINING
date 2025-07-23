flag = True

def circle():
    r = int(input("Enter the radius: "))
    print(f"Area of circle = {3.14*r*r}\n")

def square(s):
    print(f"Area of square = {s*s}\n")

def triangle():
    b = int(input("Enter the base length: "))
    h = int(input("Enter the height: "))
    return 0.5*b*h

def rectangle(l,b):
    return l*b

while flag:
    print("1. Circle\n2. Square\n3. Triangle\n4. Rectangle\n5. Exit")
    ch = int(input("Enter your choice: "))
    match ch:
        case 1:
            circle()
        case 2:
            side = int(input("Enter the length of side: "))
            square(side)
        case 3:
            res = triangle()
            print(f"Area of triangle = {res}\n")
        case 4:
            length = int(input("Enter the length: "))
            breadth = int(input("Enter the breadth: "))
            res = rectangle(length,breadth)
            print(f"Area of rectangle = {res}\n")
        case 5:
            exit()
        case _:
            print("Invalid choice")