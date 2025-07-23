amt = int(input("Enter the amount: "))
denominations = [500,200,100,50,20,10,5,2,1]
notes = []
count = []
while amt > 0:
    for i in denominations:
        pos = False
        while amt >= i:
            c = amt//i
            amt = amt - c*i
            pos = True
        if pos:
            notes.append(i)
            count.append(c)
for i in range(len(notes)):
    print(f"{count[i]} notes of Rs.{notes[i]}")