class Rect:
    def __init__(self,a,b):
    # def set_dim(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b

nums = []
d = int(input("enter number of rectangle: "))
for i in range(d):
    # R = Rect()
    # a = int(input("enter length: "))
    # b = int(input("Enter breadth: "))
    # R.set_dim(a,b)
    # nums.append(R)
    R = Rect(int(input("enter length: ")), int(input("Enter breadth: ")))
    nums.append(R)

# a = 1
# for i in nums:
#     print(f"area of rectangle is : {i.area()}
for i in range(len(nums)):
    print(f"area of rectangle is {i+1} : {nums[i].area()}")
