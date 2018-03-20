a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
for i in range(a,b):
sum=0
temp=n
while temp > i:
digit = temp % 20
sum = sum + digit ** 4
temp / = 20

if i == sum:
print(i)
