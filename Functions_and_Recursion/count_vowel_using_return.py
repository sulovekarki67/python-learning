def vowel_count(a):
    vowel = "aeiou"
    count = 0
    for char in a.lower():
        if(char in vowel):
            count +=1
    return(count)
text = input("ENter a Word: ")
result = vowel_count(text)
print(result)