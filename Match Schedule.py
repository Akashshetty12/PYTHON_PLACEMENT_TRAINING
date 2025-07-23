import random
num = int(input("Enter the number of teams: "))
teams = []
for i in range(num):
    teams.append(input(f"Enter the team name: "))
meet = int(input("Enter the number of meetings: "))
matches = []
for i in range(num-1):
    for j in range(i+1, num):
        for k in range(meet):
            matches.append(f"{teams[i]} vs {teams[j]}")
random.shuffle(matches)
for i in range(len(matches)):
    print(f"Match {i+1}: {matches[i]}")