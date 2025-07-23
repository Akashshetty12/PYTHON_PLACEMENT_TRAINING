heads = int(input("Enter the total number of heads: "))
legs = int(input("Enter the total number of legs: "))
flag = False
if legs %2 != 0:
    print("No solution")
else:
    for h in range(1,heads+1):
        c = heads - h
        if h*2 + c*4 == legs:
            print(f"Number of hens = {h}\nNumber of cows = {c}")
            flag = True
            break
        else:
            h += 1
            c -= 1
    if not flag:
        print("No solution")