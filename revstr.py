s= input("Enter String:")
chars = list(s)
left,right = 0,len(str(s))-1
while left<right:
    chars[left],chars[right]=chars[right],chars[left]
    left+=1
    right-=1
print("".join(chars))