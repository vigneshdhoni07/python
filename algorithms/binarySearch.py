ar=[56,23,9,21,37,89,105,54]
ar.sort()
print(ar)
def binarySearch(ar,x):
    u=len(ar)-1
    l=0
    while(l<=u):
        m=(l+u)//2
        if(ar[m]==x):
            return m
        elif(ar[m]<x):
            l=m+1
        else:
            u=m-1
    return -1

print(binarySearch(ar,106))