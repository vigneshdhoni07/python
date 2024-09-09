arr=[2,3,1,6,3,6,2]
freqObj={}


for i in arr:
    if(freqObj.get(i)==None):
       freqObj[i]=1
    else:
        freqObj[i]=freqObj[i]+1

print(freqObj)  

op=None
for i in freqObj:
    if(freqObj[i]==1):
        op=i
        
print(op)