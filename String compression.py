st = input("Enter the string:")
c = 1
res = ""
for i in range(len(st)):
    if i+1 < len(st) and st[i] == st[i+1]:
        c += 1
    else:
        res = res + st[i] + str(c)
        c = 1
print(res)