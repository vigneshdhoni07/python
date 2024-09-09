# arr1=[2,8,6,5,4,3]
# arr2=[2,3,4,7]
# n=6
# m=4
# arr1=[10,10]
# arr2=[10]
# n=2
# m=1
# arr1=[2,6,1,2]
# arr2=[1,2,3,4,2]
# n=4
# m=5
# arr1=[2,1,2,2]
# arr2=[2,2,2,2]
# n=4
# m=4
arr1=[6,9,8,5]
arr2=[9,2,4,1,8]
n=4
m=5


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

mergeSort(arr1,0,len(arr1)-1)
mergeSort(arr2,0,len(arr2)-1)

# not optimzed
# def IntersectionArr(arr1,arr2,n,m):
#     print(arr1)
#     print(arr2)
#     i=0
#     k=0
#     op=[]
#     while(i<n):
#         j=k
#         while(j<m):
#             if(arr1[i]==arr2[j]):
#                 op.append(arr1[i])
#                 k=j+1
#                 break
#             j+=1
#         i+=1
#     return op
            

# ans=None    
# if(n<m):
#     ans=IntersectionArr(arr1,arr2,n,m)
# else:
#     ans=IntersectionArr(arr2,arr1,m,n)
    
# print(ans)


# optimized 1
def IntersectionArr(arr1,arr2,n,m):
    i=0
    j=0
    while(i<n and j<m):
        if(arr1[i]==arr2[j]):
            print(arr1[i],end=" ")
            i+=1
            j+=1
        elif(arr1[i]>arr2[j]):
            j+=1
        else:
            i+=1   
            
# optimized 2 in this approach sort the smaller array and do binary search in smaller array with each element in other array