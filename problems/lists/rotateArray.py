ar=[1,3,6,11,12,17,22,26,30,33,38] 
def rotate(arr, n, d):
    i=0
    j=d
    while(i<d and j<n):
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j+=1
    k=d
    while(i<d):
        arr[i],arr[k]=arr[k],arr[i]
        i+=1
        k+=1
    
rotate(ar,len(ar),7)
print(ar)




