def anagram(arr):
    pairs = {}

    for group in arr:
        key = "".join(sorted(group))
        if key in pairs:
            pairs[key].append(group)
        else:
            pairs[key] = [group]
    return list(pairs.values())

print(anagram(["ate","tae","ant","tan","tea"]))
        
