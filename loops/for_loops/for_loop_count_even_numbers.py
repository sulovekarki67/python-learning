number = []
for i in range(0,5):
    num = int(input("Enter a number"))
    number.append(num)
count = 0
for r in range(0,5):
    if(number[r]%2==0):
        count=count+1
print(count)
