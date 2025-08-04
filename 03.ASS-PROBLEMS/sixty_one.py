def is_subset_sum(nums, target, index=0):
    
    if target == 0:
        return True

    if index >= len(nums) or target < 0:
        return False

    if nums[index] <= target:
        if is_subset_sum(nums, target - nums[index], index + 1):
            return True

    return is_subset_sum(nums, target, index+1)
nums = [3, 34, 4, 12, 5, 2]
target = 9

if is_subset_sum(nums, target):
    print("Subset with target sum exists!")
else:
    print("No subset with the target sum.")

