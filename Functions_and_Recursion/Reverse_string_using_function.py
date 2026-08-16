def reverse_string(text):
    reverse = ""
    for i in text:
        reverse = i + reverse
    return(reverse)    
result = reverse_string("Sulove")
print(result)