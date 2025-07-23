import random
name1 = input("Enter player 1: ")
name2 = input("Enter player 2: ")
print("The computer has fixed 5 numbers in the range 1 and 10")
print("You have 3 choices each to guess the number\nThe player with higher score wins the game.....")

nums = []
for i in range(5):
    num = random.randint(1,10)
    if num not in nums:
        nums.append(num)

ch1 = []
ch2 = []
s1 = s2 = 0

for i in range(3):
    print(f"-----ROUND{i+1}-----")
    ch = int(input(f"{name1} enter your choice: "))
    while ch in ch1 or ch in ch2:
        ch = int(input(f"It is already taken.Choose another: "))
    ch1.append(ch)
    if ch in nums:
        s1 += 1
        print("----->>Correct")
    else:
        print("----->>Wrong")
    ch = int(input(f"{name2} enter your choice: "))
    while ch in ch1 or ch in ch2:
        ch = int(input(f"It is already taken.Choose another: "))
    ch2.append(ch)
    if ch in nums:
        s2 += 1
        print("----->>Correct")
    else:
        print("----->>Wrong")
print("-----------")
print("Summary:")
print(f"Choices fixed by the computer: {nums}")
print(f"Choices entered by {name1}: {ch1}")
print(f"Score of {name1}:{s1}")
print(f"Choices entered by {name2}: {ch2}")
print(f"Score of {name2}:{s2}")

if s1>s2:
    print(f"{name1} is the WINNER")
elif s2>s1:
    print(f"{name2} is the WINNER")
else:
    print("It's a DRAW")
print("-----GAME OVER-----")