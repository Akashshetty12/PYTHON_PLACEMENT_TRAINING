def get_digits(n):
    digits = []
    while n != 0:
        digits.append(n%10)
        n = n//10
    return digits

def isprime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def digits_isprime(n):
    digits = get_digits(n)
    for i in digits:
        if not isprime(i):
            return False
    return True
for i in range(100,1000):
    if isprime(i) and isprime(sum(get_digits(i))) and digits_isprime(i):
        print(i,end=' ')