blocks = int(input("Enter the number of blocks: "))
lines = int(input("Enter the number of lines: "))
stars = int(input("Enter the number of stars: "))
total = 0
print("---------------------")
for i in range(blocks):
    print(f"-----Block{i+1}-----")
    count = 0
    for j in range(lines - i):
        print("* "*stars)
        total += stars
        count += stars
    print(f"Number of stars = {count}")
print("---------------------")
print(f"Total number of stars = {total}")