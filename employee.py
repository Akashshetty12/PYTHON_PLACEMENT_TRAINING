class Emp:
    profit = 1000000
    tax = 10
    company = "COGNIZANT"
    def __init__(self,name,age,sal,per):
        self.name = name
        self.age = age
        self.sal = sal
        self.per = per
        self.share_amount = 0
        self.tax_amount = 0

    def cal_tax(self):
        return int((Emp.tax/100) * self.sal)

    def cal_share(self):
        return int((self.per/100) * self.sal)

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Sal:",self.sal)
        print("Tax:",self.cal_tax())
        print("Company:",self.company)
        print("share:",self.cal_share())
        print("Net Salary:",self.take_home())

    def take_home(self):
        return int(self.sal - self.cal_tax() + self.cal_share())

e1 = Emp("Sachin",40,50000,4 )
e1.cal_tax()
e1.cal_share()
e1.take_home()
e1.display()
print("------------------")
e2 = Emp("Suraj",45,60000,6 )
e2.cal_tax()
e2.cal_share()
e2.take_home()
e2.display()
print("-------------------")
e3 = Emp("Manu",30,30000,3 )
e3.display()
