total = 0
while True:
    num = int(input("Enter mark:"))
    if num > 100:
        continue
    elif num == 0:
        break
    else:
        total += num
print(f"Total marks = {total}")