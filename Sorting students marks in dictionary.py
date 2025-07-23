students = [
    {"name": "raju", "dept": "cse", "marks": [20, 30, 40]},
    {"name": "vijay", "dept": "cse", "marks": [10, 70, 43]},
    {"name": "pavi", "dept": "ece", "marks": [22, 38, 56]},
    {"name": "rose", "dept": "ece", "marks": [26, 36, 89]},
    {"name": "virat", "dept": "ece", "marks": [16, 90, 43]}
]

for i in students:
    i["per"] = sum(i["marks"])/len(i["marks"])

sorted_students = sorted(students, key= lambda x: x["per"],reverse=True)
des = ["FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH"]
index = 1

for i in sorted_students:
    print(f"{index}. {i["name"]} stands {des[index-1]} : {i["per"]:.2f}%")
    index += 1