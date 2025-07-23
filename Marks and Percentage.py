names = []
marks = []
perc = []
for i in range(5):
    names.append(input("Enter the name: "))
    for j in range(3):
        marks.append(int(input("Enter the marks: ")))

for i in range(5):
    tot = 0
    for j in range(3):
        tot += marks.pop()
    perc.append(tot//300*100)
print()
for i in range(5):
    print(f"{i+1}.{names[i]}: {perc[4-i]}%")