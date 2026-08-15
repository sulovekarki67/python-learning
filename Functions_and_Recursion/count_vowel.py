def count_vowel(a):
    vowel = "aeiou"
    count = 0
    for char in a.lower(): 
        if(char in vowel):
            count = count + 1
    print(count)
text = input("Enter a text: ")
count_vowel(text)