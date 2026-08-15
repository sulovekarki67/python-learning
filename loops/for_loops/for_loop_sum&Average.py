number = []
sum = 0
for i in range(0,5):
    num = int(input("Enter a number: "))
    number.append(num)
    sum= sum + num
avg = (sum/5)
print(f"sum: {sum}")
print(f"average: {avg}")
