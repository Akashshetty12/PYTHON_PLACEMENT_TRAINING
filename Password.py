s = input("Enter your password: ")
dg = up = lw = sp = cont = False
chars = []
if len(s)>7:
    for i in s:
        chars.append(i.lower())
        if i.isupper():
            up = True
        elif i.islower():
            lw = True
        elif i.isdigit():
            dg = True
        else:
            sp = True
    for i in range(len(chars)-1):
        if chars[i] == chars[i+1]:
            cont = True
    if up and dg and sp and not cont:
        print("Good password")
    else:
        print("Bad password")
else:
    print("Bad password(less number of characters)")