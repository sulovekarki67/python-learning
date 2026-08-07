e = int(input("Enter english marks:"))
m = int(input("Enter math marks:"))
c = int(input("Enter computer marks"))
total = ((e+m+c)/300)*100
if(m>=32 and e>=32 and c>=32 and total>=40):
  print("passed")
else: 
  print("failed")
