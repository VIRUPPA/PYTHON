def numbers(arr):
    negative = []
    positive = []

    for i in arr:
        if i >= 0:
          positive.append(i)
        elif i < 0:
          negative.append(i)
    
    output = negative + positive
    output.sort()
    return output

arr = [1,3,-2,-5,6,-9,2]
print(numbers(arr))
