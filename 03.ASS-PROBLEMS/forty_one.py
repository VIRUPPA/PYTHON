def split_list(arr):
    total = sum(arr)
    if total % 2 != 0:
        return false
    target = total //2
    n = len(arr)
    dp = [False] * (target + 1)
    dp[0] = True

    for num in arr:
        for i in range(target,num-1,-1):
            dp[i] = dp[i] or dp[i - num]
    return dp[target]

print("testcase1 :",split_list([1,5,11,5])
print("testcase2 :",split_list([2,3,4,61])
    
