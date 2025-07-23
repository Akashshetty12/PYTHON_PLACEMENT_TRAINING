from datetime import datetime
a = input("Enter first date: ")
b = input("Enter second date: ")
d1 = datetime.strptime(a,"%d-%m-%Y")
d2 = datetime.strptime(b,"%d-%m-%Y")
diff = d2 - d1
print(f"Difference: {abs(diff.days)} days")