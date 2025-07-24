from pydoc_data.topics import topics

# tall tower heigh is x meter
# there is monkey at the bottom of tower
# from bttom monkey has to reach top
# top in 1 min 10 m , slip 5m in next min minimum time req to reach the top od tower

# x = 30
# a = 10
# b = 5

def cal(x,a,b):
    return 2 * (x - a) / (a - b) + 1
    # time = 0
    # distance = 0
    # while True:
    #     if distance != x:
    #         time = time + 1
    #         distance = distance + a
    #     if distance == x:
    #         return time
    #     else:
    #         distance = distance - b
    #         time = time +

print(cal(30,10,5))
print(cal(25,7,4))