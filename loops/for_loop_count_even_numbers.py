number = []
for i in range(1,6):
    num = int(input("Enter a number"))
    number.append(num)
count = 1
for r in range(0,6):
    check = number[r]
    if(check%2==0):
        count=count+1
