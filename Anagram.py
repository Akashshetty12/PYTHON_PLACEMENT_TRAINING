s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")

s1 = s1.replace(" ","")
s2 = s2.replace(" ","")

s1 = s1.lower()
s2 = s2.lower()

s1 = sorted(s1)
s2 = sorted(s2)

if s1 == s2:
    print("Given strings are anagram")
else:
    print("Given strings are not anagram")