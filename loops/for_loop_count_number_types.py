number = []
for i in range(0,5):
    num = int(input("Enter a Number "))
    number.append(num)
positive = 0 
negative = 0
zero = 0
for r in range(0,5):
    if(number[r]>0):
        positive = positive + 1
    elif(number[r]<0):
        negative = negative + 1
    else:
        zero = zero + 1
print(f"positive: {positive}")
print(f"Negative: {negative}")
print(f"Zero: {zero}")
