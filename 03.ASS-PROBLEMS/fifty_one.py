def unique(arr1,arr2):
    value1 = []
    value2 = []

    for word in arr1:
        if word not in arr2:
            value1.append(word)

    for word in arr2:
        if word not in arr1:
            value2.append(word)

    return value1,value2 


first =[2,2,2,2,3,4]
second =[4,6,7,8]
unique1,unique2 = unique(first,second)
print("element of value same:",unique1)
print(unique2)
