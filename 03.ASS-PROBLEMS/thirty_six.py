def move_zeros_to_end(arr):
    result = []

    for num in arr:
        if num != 0:
            result.append(num)

    zeros = arr.count(0)
    result.extend([0] * zeros)

    return result

arr = [0, 1, 4, 0, 6, 3, 7, 9]
print(move_zeros_to_end(arr))
 
