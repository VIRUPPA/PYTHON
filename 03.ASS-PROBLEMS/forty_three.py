def can_partition_k_subsets(arr, k):
    total = sum(arr)

    if total % k != 0:
        return False

    target = total // k
    used = [False] * len(arr)
    arr.sort(reverse=True)  

    def backtrack(start, k_remaining, current_sum):
        if k_remaining == 1:
            return True 

        if current_sum == target:
            return backtrack(0, k_remaining - 1, 0)

        for i in range(start, len(arr)):
            if not used[i] and current_sum + arr[i] <= target:
                used[i] = True
                if backtrack(i + 1, k_remaining, current_sum + arr[i]):
                    return True
                used[i] = False

                if current_sum == 0:
                    break

        return False

    return backtrack(0, k, 0)

print(can_partition_k_subsets([4, 3, 2, 3, 5, 2, 1], 4))
print(can_partition_k_subsets([1, 2, 3, 4], 3))     
print(can_partition_k_subsets([2, 1, 4, 5, 6], 3))        
print(can_partition_k_subsets([1, 1, 1, 1, 1, 1], 3))     

