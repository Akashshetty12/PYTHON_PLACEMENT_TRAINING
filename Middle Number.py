num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
num3 = int(input("Enter the num3: "))
if num1 >= num2 and num1 <= num3:
    print(f"{num1} is the middle number")
elif num2 >= num1 and num2 <= num3:
    print(f"{num2} is the middle number")
else:
    print(f"{num3} is the middle number")