ar=[2,1,0,1,2,0]
def sort012(arr, n) :
   p0=0
   p2=n-1
   s=0
   e=n-1
   while(s<e):
       if(arr[s]==0):
           arr[s],arr[p0]=arr[p0],arr[s]
           p0+=1
       if(arr[e]==0):
           arr[e],arr[p0]=arr[p0],arr[e]
           p0+=1
       s+=1
       e-=1        
       if(arr[s]==2):
           arr[s],arr[p2]=arr[p2],arr[s]
           p2-=1
       if(arr[e]==2):
           arr[e],arr[p2]=arr[p2],arr[e]
           p2-=1
        
       s+=1
       e-=1

sort012(ar,len(ar))
print(ar)