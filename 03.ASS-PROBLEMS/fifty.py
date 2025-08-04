def edit_away(s1,s2):
 
    if abs(len(s1) - len(s2)) > 1:
        return False 

    if len(s1) > len(s2):
         s1,s2 = s2,s1

    hashmap = {}
    for char in s1:
        if char in hashmap:
              hashmap[char] += 1
        else:
              hashmap[char] = 1
    edit_count = 0 
    for char in s2:
        if char in hashmap and hashmap[char] > 0:
            hashmap[char] -= 1 
        else:
            edit_count += 1 
            if edit_count > 1:
                return False 
    return True 

print(edit_away("pale", "ple"))
print(edit_away("pales", "pale"))   
print(edit_away("pale", "bale"))    
print(edit_away("pale", "bake"))    
print(edit_away("abc", "abcc"))     

