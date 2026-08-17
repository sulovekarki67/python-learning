def square(num):
    return (num ** 2)

def add_square(a,b):
    a_square = square(a)
    b_square = square(b)
    return(a_square + b_square)

result = add_square(3,4)
print(result)