import string
def remove_punctuation(text):
    result = ""
    for ch in text:
        if ch not in string.punctuation:
            result += ch
    return result

def build_frequency_dict(text):

    clean_text = remove_punctuation(text)

    clean_text = clean_text.lower()
    words = clean_text.split()

    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency
text = "Hello, hello! World? Hello world."
freq_dict = build_frequency_dict(text)
print(freq_dict)

