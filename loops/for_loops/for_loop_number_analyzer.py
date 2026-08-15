number = []
value = int(input("how many number do you want to Enter..? : "))
for i in range(0,value):
    num = int(input("Enter a number: "))
    number.append(num)
smallest = number[0]
for a in range(0,value):
    if(number[a]<smallest):
        smallest = number[a]
largest = number[0]
for b in range(0,value):
    if(number[b]>largest):
        largest = number[b]
sum = 0
for c in range(0,value):
    sum = sum + number[c]
even = 0
odd = 0
for d in range(0,value):
    if(number[d]%2==0):
        even = even + 1
    else:
        odd = odd +1
print(f"Largest: {largest}")
print(f"Smallest: {smallest}")
print(f"Sum: {sum}")
print(f"Even number: {even}")
print(f"Odd number: {odd}")