num=int(input("Enter number:"))
count=0
temp=num
while temp>0:
    digit=temp%10
    print(digit)
    count+=1
    temp=temp//10
print("The total nums are:",count)