arr=[0,7,2,5,4,7,1,3,6]
freqObj={}


for i in arr:
    if(freqObj.get(i)==None):
       freqObj[i]=1
    else:
        freqObj[i]=freqObj[i]+1

print(freqObj)  

op=None
for i in freqObj:
    if(freqObj[i]>1):
        op=i
        
print(op)