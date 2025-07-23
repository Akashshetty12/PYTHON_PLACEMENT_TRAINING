boy = input("Enter boy name: ")
girl = input("Enter girl name: ")
b = list(boy)
g = list(girl)
for i in range(len(b)):
    for j in range(len(g)):
        if b[i] == g[j]:
            b[i] = g[j] = '2'
for i in b:
    if i=='2':
        b.remove(i)
for i in g:
    if i=='2':
        g.remove(i)

num = len(b)+len(g)
index = 0
ans = ['F','L','A','M','E','S']
while len(ans) > 1:
    index = (index+(num-1))%len(ans)
    ans.pop(index)
print(f'The relation is {ans[0]}')