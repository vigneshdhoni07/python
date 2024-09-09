a=[1,3,5,6,7,8,9,25]

def binS(arr,v,s,e):
    if(s>e):
        return -1
    m=(s+e)//2
    if(arr[m]==v):
        return m
    if(arr[m]<v):
        s=m+1
    if(arr[m]>v):
        e=m-1
    return binS(arr,v,s,e)
        
print(binS(a,3,0,len(a)-1))