number = []
for i in range(0,5):
    num = int(input("Enter a number"))
    number.append(num)
largest = number[0]
for r in range(0,5):
 if (number[r]>largest):
    largest = number[r]
print(f"Largest number: {largest}")
