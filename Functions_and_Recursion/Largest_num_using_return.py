def maximum(a,b):
    if(a>b):
        return(a)
    elif(a<b):
        return(b)
    else:
        return("equal")
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
result = maximum(num1,num2)
print(result)