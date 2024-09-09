arr=[2,13,4,1,3,6,28]

i=1

while(i<len(arr)):
    
    j=i-1
    temp=arr[i]    #4
    
    while(j>=0 and arr[j]>temp):
          arr[j+1]=arr[j]
          j-=1
    arr[j+1]=temp        
    i+=1
    
    

print(arr)
        
        
            