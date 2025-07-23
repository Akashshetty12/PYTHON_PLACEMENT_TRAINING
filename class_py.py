# class LC37:
#     def student(self,name):
#         self.name = name
#         #self is the  constructor which calls itself
#
#
#     def display(self):
#         self.nature()
#         print(f"The name is {self.name}")
#
#     def nature(self):
#         print(f"{self.name} is a food boy")
#
# a1 = LC37()
# a2 = LC37()
# a1.student("Rohit")
# a2.student("Mohit")
# a1.display()
# a2.display()
# a1.nature()
# a2.nature()

# if you want to use Methods are variable we have to use either object name or class name in the main

class College:
    def student(self, name, mark):
        self.name = name
        self.mark = mark

    def passfail(self):
        if self.mark >= 40:
            print(f"pass")
        else:
            print(f"fail")
    def modify(self, grace):
        self.mark = self.mark + grace

    def display(self):
        print(f" Name : {self.name}")
        print(f" Mark : {self.mark}")
        print(f"College: {self.col}")
        self.passfail()

s1 = College()
s2 = College()
s1.student("Rohit", 30)
s2.student("Mohit", 60)
s1.display()
print("-----------")
s2.display()
print("-----------")
s1.modify(20)
s1.display()
