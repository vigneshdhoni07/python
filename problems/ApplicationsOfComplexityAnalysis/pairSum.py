
def pairSum(arr, n, num) :
    # write your code logic here !!
    # Try to submit your code in O(n * log(n)) Time complexity.
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

        mergeSort(arr,0,len(arr)-1)
        count=0
        ar2=[] 
        freqObj={}
        for i in arr:
            if(freqObj.get(i)==None):
                freqObj[i]=1
                ar2.append(i)
            else:
                freqObj[i]=freqObj[i]+1

        s=0
        e=len(ar2)-1
        while(s<=e):
            if(ar2[s]+ar2[e]==num):
                if(s==e):
                    y=freqObj[ar2[s]]
                    z=0
                    b=False
                    for k in range(1,y):
                        z+=k
                        b=True
                    if(b):
                        count+=z
                else:     
                    a=freqObj[ar2[s]]
                    b=freqObj[ar2[e]]
                    c=a*b
                    count+=c  
                s+=1
                e-=1
            
            elif(ar2[s]+ar2[e]>num):
                e-=1
            elif(ar2[s]+ar2[e]<num):
                s+=1               
        return count
