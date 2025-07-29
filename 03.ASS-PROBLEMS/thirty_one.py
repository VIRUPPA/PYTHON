def rotation(a,b):
    if len(a) != len(b):
        return False 

    n = len(a)

    for i in range(n):
        wire = a[i:] + a[:i]
        if wire == b:
          return True

    return False 

print(rotation([1,2,3,4,5,6],[4,5,6,1,2,3]))
