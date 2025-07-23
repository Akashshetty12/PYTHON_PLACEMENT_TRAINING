names = ["A","B","C","D","E","F","G","H","I","J"]
memos = [0,1,1,1,2,2,1,2,1,2]
salary = [1000,2000,3000,4500,2000,5000,1500,2300,1300,1100]

c = 0
fire=[]
emp_list = list(zip(names,memos,salary))
for i in emp_list:
    if i[2] > 4000:
        emp_list.remove(i)
        fire.append(i)
        c += 1
emp_list = sorted(emp_list,key= lambda x: x[2],reverse=True)
for i in emp_list:
    if c<5:
        if i[1] >=2:
            emp_list.remove(i)
            fire.append(i)
            c += 1
print("Employees to be fired:")
for i in range(len(fire)):
    print(f"{i+1}. Name:{fire[i][0]}, Memos:{fire[i][1]}, Salary:{fire[i][2]}")