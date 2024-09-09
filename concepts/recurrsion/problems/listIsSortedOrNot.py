n=[1,3,4,5,6,9]

def checkSorted(arr,i):
    if(i==0):
        return True
    if(arr[i]<arr[i-1]):
        return False
    op=checkSorted(arr,i-1)
    return op

print(checkSorted(n,len(n)-1))