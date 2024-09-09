a=[3,1,6,9,4,5,30,27]

def mergeSort(arr,i,j):
    if(i>=j):
        return
    mergeSort(arr,i,(i+j)//2)
    mergeSort(arr,((i+j)//2)+1,j)
    return conquer(arr,i,(i+j)//2,j)

def conquer(ar,i,m,j):
    ar2=[]
    s1=i
    e1=m
    s2=m+1
    e2=j
    # print(ar[i:j+1],"ip",s1,e1,s2,e2)
    while(s1<=e1 and s2<=e2):
        if(ar[s1]<ar[s2]):
            ar2.append(ar[s1])
            s1+=1
        else:
            ar2.append(ar[s2])
            s2+=1
    
    while(s1<=e1):
        ar2.append(ar[s1])
        s1+=1
    while(s2<=e2):
        ar2.append(ar[s2])
        s2+=1    
    ss=0
    ee=len(ar2)-1
    while(ss<=ee):
        ar[i+ss]=ar2[ss]
        ss+=1
    return
        

mergeSort(a,0,len(a)-1)
print(a)