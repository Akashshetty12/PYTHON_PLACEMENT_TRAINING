num = int(input("Enter a number"))
c = 0
for i in range(2,num//2):
    if num%i == 0:
        c += 1
if c == 0:
    print("It is prime")
else:
    print("It is composite")