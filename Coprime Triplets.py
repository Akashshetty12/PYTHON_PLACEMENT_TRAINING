n = int(input("Enter a number: "))

def gcd(a,b):
    while b!=0:
        rem = a%b
        a = b
        b = rem
    return a

def cop(a,b):
    return gcd(a,b) == 1

for i in range(1,n):
    for j in range(1,i):
        for k in range(1,j):
            if (i*i == j*j+k*k) and cop(i,j) and cop(j,k) and cop(i,k):
                print(k,j,i)