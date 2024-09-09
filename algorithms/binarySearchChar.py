ar=['n','q','a','t','e','k','s','i']
ar.sort()
print(ar)
def binarySearchChar(ar,x:chr)->int:
    x=ord(x)
    u=len(ar)-1
    l=0
    while(l<=u):
        m=(l+u)//2
        if(ord(ar[m])==x):
            return m
        elif(ord(ar[m])<x):
            l=m+1
        else:
            u=m-1
    return -1

print(binarySearchChar(ar,'t'))