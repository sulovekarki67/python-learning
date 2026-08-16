def count_even(numbers):
    count = 0
    for i in numbers:
        if (i % 2 == 0):
            count += 1
    return(count)
result = count_even([343,3434,223,34,21])
print(result)