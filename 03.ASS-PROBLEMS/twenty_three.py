from collections import Counter

s = input("Enter a string: ")

freq = Counter(s)

counts = freq.values()

odd_count = 0
for count in counts:
    if count % 2 != 0:
        odd_count += 1

if odd_count <= 1:
    print("Yes, it can be rearranged to form a palindrome.")
else:
    print("No, it cannot be rearranged to form a palindrome.")


