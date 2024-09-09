arr=[1,3,6,2,5,4,3,2,4]
x=7
arr.sort()
print(arr)
def pairsum(ar,n,x):
    c=0
    # s=0
    # e=n-1
    # while(s<e):
    #     if(ar[s]+ar[e]==x):
    #         c+=1
    #         if(ar[s]==ar[s+1] and ar[e] !=ar[e-1]):
    #             s+=1
    #             continue
    #         if(ar[e]==ar[e-1] and ar[s]!=ar[s+1]):
    #             e-=1
    #             continue
    #         s+=1
    #         e-=1
    #     elif(ar[s]+ar[e]>x):
    #         e-=1
    #     else:
    #         s+=1
    for i in range(n):
        for j in range(i+1,n):
            if(ar[i]+ar[j]==x):
                c+=1
    return c

print(pairsum(arr,len(arr),7))         