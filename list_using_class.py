class abc():
    def dis(self,a,b):
        self.a = a
        self.b = b
    def greet(self):
        print("good morning")

z = abc()
x = abc()
lst = []
z.dis(20,30)
x.dis(50,40)
lst.append(z)
lst.append(x)
print(lst[0].b)