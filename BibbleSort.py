def bubbleSort(element):
    for i in range(len(element)):
        for j in range(len(element)-i-1):
            if element[j] > element[j+1]:
                element[j], element[j+1] = element[j+1], element[j]
    return element

element = [10,12,2,5,7,100,87]
res = bubbleSort(element)
print(res)