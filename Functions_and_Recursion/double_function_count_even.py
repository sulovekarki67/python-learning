def is_even(num):
    if(num % 2 == 0):
        return(True)
    else:
        return(False)

def count_even(a):
    count = 0
    for i in a:
     if (is_even(i)):
        count = count + 1
    return(count)
num = [1,2,3,4,5,65,2]   
result = count_even(num)
print(result)