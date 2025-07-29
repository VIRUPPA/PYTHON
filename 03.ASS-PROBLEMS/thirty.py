mind = [1,2,3,4,5,6,7,8,9]
k = 5
count = 0 
start = 0 

a = len(mind)
k = k % a

while count < a:
    current = start 
    prev = mind[start]

    while True:
        peace = (current + k ) % a 
        mind[peace],prev = prev,mind[peace]
        current = peace 
        count += 1 

        if start == current:
            break
    start += 1

print(mind)

