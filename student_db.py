# main menu :
# 1. add new student -> name, marks in 3 subject
# 2. view status
# 3. exit
#
# status menu:
# 1 view topper with percentage
# 2 individual mark
# 3 main menu

class student:
    def __init__(self, name, roll_no, m1, m2, m3):
        self.name = name
        self.roll_no = roll_no
        self.perc = (m1 + m2 + m3) / 3
        self.marks = {"OS": m1, "DS": m2, "CA": m3}
        self.details = {"name": self.name, "Roll no": self.roll_no, "Marks": self.marks, "Percentage": self.perc}


class handle:
    def __init__(self, students):
        self.students = students

    def update_rank(self):
        self.sorted_students = sorted(self.students, key=lambda x: x.perc, reverse=True)
        rank = 1
        for i in self.sorted_students:
            i.details["Rank"] = rank
            rank += 1

    def top(self):
        print(f"\n{self.sorted_students[0].name} is the topper\nPercentage: {self.sorted_students[0].perc}\n")

    def display(self, roll_no):
        flag = False
        for i in self.sorted_students:
            if roll_no == i.roll_no:
                flag = True
                print(f"\nName: {i.details['name']}")
                print(f"Marks: {i.details['Marks']}")
                print(f"Percentage: {i.details['Percentage']}")
                print(f"Rank: {i.details['Rank']}\n")
        if not flag:
            print("Student not found")


students = []

while True:
    print("1.Add student\n2.View status\n3.Exit")
    ch = int(input("Enter the choice: "))
    if ch == 1:
        name = input("Enter the name: ")
        roll_no = int(input("Enter the roll number: "))
        m1 = int(input("Enter marks in OS: "))
        m2 = int(input("Enter marks in DS: "))
        m3 = int(input("Enter marks in CA: "))
        s = student(name, roll_no, m1, m2, m3)
        students.append(s)
        print("Details added successfully")
        han = handle(students)
        han.update_rank()
    elif ch == 2:
        roll_no = int(input("Enter roll number: "))
        while True:
            print("1.View Topper\n2.Check individual details\n3.Back to main menu")
            c = int(input("Enter your choice: "))
            if c == 1:
                han.top()
            elif c == 2:
                han.display(roll_no)
            elif c == 3:
                break
            else:
                print("Invalid choice")
    elif ch == 3:
        break
    else:
        print("Invalid choice")