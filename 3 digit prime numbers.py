n = int(input("Enter the number of integers required: "))
count = 0
for i in range(100,1000):
    prime = True
    for j in range(2,i):
        if i % j == 0:
            prime = False
    if prime:
        if count < n:
            print(i,end=' ')
        count += 1