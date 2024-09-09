arr=[1, 4, 9, 3, 2]



for i in range(0,len(arr)-1):
    sum=arr[i]+arr[i+1]
    arr[i+1]=sum
    
def equiIndex(arr):
    i=1
    e=len(arr)-1
    while(i<e):
        f=arr[i-1]
        l=arr[e]-arr[i]
        if(f==l):
            return i
        i+=1
    return -1

print(equiIndex(arr))