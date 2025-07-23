matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

l = 0
r = len(matrix[0])-1
t = 0
b = len(matrix)-1

while t<=b and l<=r:
    for i in range(l,r+1):
        print(matrix[t][i],end=' ')
    t += 1
    for i in range(t,b+1):
        print(matrix[i][r],end=' ')
    r -= 1
    if l<=r:
        for i in range(r,l-1,-1):
            print(matrix[b][i],end=' ')
        b -= 1
    if t<=b:
        for i in range(b,t-1,-1):
            print(matrix[i][l],end=' ')
        l += 1