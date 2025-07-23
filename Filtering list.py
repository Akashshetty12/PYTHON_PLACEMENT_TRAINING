notorious = ["Darshan","Rohit","Anuj"]
names = ["Anu","Darshan","Rohit","Jack","Priya","Bala","Rai","Ram","Raj","Ben"]
score = [2,5,6,8,3,5,6,9,8,2]
filtered = []
for i in range(10):
    if score[i]>5:
        if names[i] not in notorious:
            filtered.append(names[i])
print(filtered)