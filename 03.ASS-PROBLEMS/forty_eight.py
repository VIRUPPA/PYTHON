def frequent(steam):
    freq = {}
    value = 0 
    value1 = None 

    for num in steam:
        if num in freq:
            freq[num] += 1 
        else:
            freq[num] = 1

        if freq[num] > value:
            value = freq[num]
            values = num
    return value,values

steam = [2,3,3,2,3,5,3,2,4,3]
print(frequent(steam))

