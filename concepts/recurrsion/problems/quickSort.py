import sys
# sys.setrecursionlimit(15)

a=[3,5,1,2,7,4,28,19,38,17,39]

def quick(a,i,j):
    if(i>=j):
        return
    p=pivot(a,i,j)
    quick(a,i,p-1)
    quick(a,p+1,j)
    
def pivot(a,i,j):
    pi=a[j]
    pp=i
    it=i
    while(it<=j):
        if(a[it]<=pi):
            
            a[it],a[pp]=a[pp],a[it]
            
            it+=1
            pp+=1

        else:
            it+=1

    return pp-1

quick(a,0,len(a)-1)
print(a)