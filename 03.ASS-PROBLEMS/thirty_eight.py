def index(arr):
    total_sum = sum(arr)
    left_value = 0 
    
    for i in range(len(arr)):
        right_value = total_sum - left_value - arr[i]
          
        if left_value == right_value:
              return i

        left_value += arr[i]

    return -1 

arr = [2,4,6,8,10,12]
print(index(arr))
