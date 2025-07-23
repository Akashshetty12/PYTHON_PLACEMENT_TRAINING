num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))
'''if num1 % num2 == 0 or num2 % num1 == 0:
    print('LCM = ',max(num1,num2))
else:
    print(f'LCM = {num1*num2}')'''
big = max(num1,num2)
step = big
while True:
    if big%num1 == 0 and  big%num2 == 0:
        print(f"LCM = {big}")
        break
    else:
        big += step