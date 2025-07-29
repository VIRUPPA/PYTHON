def majorityElement(arr):

    n = len(arr)  
    for i in range(n):
        count = 0

        for j in range(n):
            if arr[i] == arr[j]:
                count += 1

        if count > n // 2:
            return arr[i]


    return -1
arr = [1, 1, 2, 1, 3, 5, 1]
print(majorityElement(arr))
