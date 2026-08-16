def letter_counter(text,target):
    count = 0
    for i in text.lower():
        if( i == target.lower()):
            count = count + 1
    return(count)
word = input("Enter a Word: ")
letter = input("Enter a Letter to Count: ")
result = letter_counter(word,letter)
print(f"{letter} appers {result} times")