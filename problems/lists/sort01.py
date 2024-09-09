arr=[0,1,1,0,1,0,1]

def sort01(ar,n):
    pivot=0
    for i in range(n):
        if(ar[i]==0):
            temp=ar[i]
            ar[i]=ar[pivot]
            ar[pivot]=temp
            pivot+=1
    
sort01(arr,len(arr))
print(arr)