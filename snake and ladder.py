import random

def gen_int():
    return random.randint(1,6)

def is_completed(pos):
    return pos == 100

snakes = {22:6, 45:30, 96:64}
ladders = {7:24, 21:77, 42:90, 40:60}

p1 = 0
p2 = 0
while True:
    p = int(input("Enter player no:"))
    if p == 1:
        num = gen_int()
        print(f"Rolled number is : {num}")
        if p1 + num > 100:
            print(f"Position of player one is : {p1}")
            print(f"Position of player two is : {p2}")
            continue
        else:
            p1 += num
            if is_completed(p1):
                print("!!!PLAYER 1 IS WINNER!!!")
                break
            elif p1 in snakes.keys():
                print("You got Snakes")
                p1 = snakes[p1]
            elif p1 in ladders.keys():
                print("GOT A LADDER!!!")
                p1 = ladders[p1]
        print(f"Position of player one is : {p1}")
        print(f"Position of player two is : {p2}")

    elif p == 2:
        num = gen_int()
        print(f"Rolled number is : {num}")
        if p2 + num > 100:
            print(f"Position of player one is : {p1}")
            print(f"Position of player two is : {p2}")
            continue
        else:
            p2 += num
            if is_completed(p2):
                print("!!!PLAYER 2 IS WINNER!!!")
                break
            elif p2 in snakes.keys():
                print("Got snake")
                p2 = snakes[p2]
            elif p2 in ladders.keys():
                print("GOT LADDER")
                p2 = ladders[p2]
        print(f"Position of player one is : {p1}")
        print(f"Position of player two is : {p2}")
    else:
        print("Invalid input")