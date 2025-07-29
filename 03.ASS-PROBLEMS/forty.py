def findmissing(arr,n):
    count = [0] * (n+1)
    for num in arr:
        count[num] += 1
    
    for i in range(1,n+1):
        if count[i] == 0:
            missing = i
        elif count[i] > 1:
            repeating = i

    print("Repeating number:", repeating)
    print("Missing number:", missing)

n = int(input("Enter a number:"))
arr = list(map(int,input("Enter a value:").split()))

findmissing(arr,n)

