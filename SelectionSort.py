def selectionSort(element):
    for i in range(len(element)):
        min = element[i]
        for j in range(i+1,len(element)):
            if element[j] < min:
                min, element[j] = element[j], min
        element[i] = min
    return element
element = [10,12,2,5,7,100,87]
res = selectionSort(element)
print(res)