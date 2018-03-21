num=int(input("Enter the digit value:")
v=num
while(v!=0):
digit=v%10
result +=digit*digit*digit
v =v/10
if(result == num):
print(armstong)
else:
print(no armstrong)
