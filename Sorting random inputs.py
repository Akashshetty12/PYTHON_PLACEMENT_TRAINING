inp = [10,11,"Zakir","Bala",123,44,53,"Anu",20,46,7,"Jack"]
even = []
odd = []
st = []
for i in inp:
    if type(i) == int:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    else:
        st.append(i)
odd.sort()
even.sort()
st.sort()
res = odd + even + st
print(res)