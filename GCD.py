num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))
if num2 > num1:
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
while num2 != 0:
    rem = num1 % num2
    num1 = num2 
    num2 = rem
print(f"GCD = {num1}")