def repeated(arr):
    seen = []
    words = arr.split()
    
    for word in words:
        if word in seen:
            return word
        seen.append(word)
    return None 
print(repeated("hello  hello"))
print(repeated("hiihii"))

