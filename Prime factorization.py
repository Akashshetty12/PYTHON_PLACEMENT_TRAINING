'''def fac(n):
    for i in range(2,n+1):
        if n%i == 0:
            print(i,end=' ')
            fac(n//i)
            break
    
n = int(input("Enter a number:"))
fac(n)'''
def fac(n):
    if n == 1:
        return
    i = 2
    while n%i != 0:
        i += 1
    print(i,end=' ')
    fac(n//i)

n = int(input("Enter a number:"))
fac(n)