def length(arr):
    n = len(arr)
    if n == 0:
        return 0 

    dp = [1] * n 
    for i in range(1,n):
        for j in range(i):
            if arr[i] >  arr[j]:
                dp[i] = max(dp[i],dp[j] +1)
   
    return max(dp)

arr = [9,5,4,6,3,2,3,1242,32131]
print(length(arr))



