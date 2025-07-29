def zero(arr):
     
    arr = list(map(str,arr))

    arr.sort(key = lambda x : x*10,reverse = True)

    if arr[0] == 0:
       return 0

    return"".join(arr)

print(zero([1,2,4,6,7,34,9325,23543]))
