n = int(input("Enter the number: "))
l = []
round = False
while n not in l:
    l.append(n)
    n = sum([int(i)*int(i) for i in str(n)])
if n ==1:
    round = True
print(round)