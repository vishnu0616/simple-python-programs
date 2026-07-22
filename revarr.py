

arr=list(map(int,input("Enter elements : ").split()))

a,b=0,len((arr))-1

while a<b:
     arr[a],arr[b]=arr[b],arr[a]
     a+=1
     b-=1
print(arr)