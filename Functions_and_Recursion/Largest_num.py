def maximum(a,b):
    if(a>b):
        print(f"{a} is largest number")
    elif(a==b):
        print("Both are equal!!")
    else:
        print(f"{b} is largest number")
num_1 = int(input("Enter a 1st number: "))
num_2 = int(input("Enter a 2nd number: "))
maximum(num_1,num_2)