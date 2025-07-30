#arr = [9,2,3,1,3,10,17]
#arr.sort(reverse=True)
#print(arr)

def loop(n):

    while n >= 3:
        n -= 3
    return n == 0

print(loop(15))
