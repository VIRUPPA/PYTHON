def findlargest(arr):
    first = second = third = arr[0]

    for num in arr:
        if num > first:
            third = second
            second = first
            first = num
        elif num > second and num != first:
            third = second
            second = num
        elif num > third and num != second and num != first:
            third = num

    print("First largest:", first)
    print("Second largest:", second)
    print("Third largest:", third)


findlargest([20,30,70,90,110])

          

         
        
