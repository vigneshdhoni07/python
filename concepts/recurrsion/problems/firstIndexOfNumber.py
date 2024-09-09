n=[2,3,4,1,2,3,6,3,7,8,5,3]

def firstOccurenceOfX(arr,x,i,l):
    if(i==l):
        return -1
    if(arr[i]==x):
        return i
    return firstOccurenceOfX(arr,x,i+1,l)

print(firstOccurenceOfX(n,4,0,len(n)))