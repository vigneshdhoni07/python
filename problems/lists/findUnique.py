li=[1,1,5]

op=0
skip=-1
for i in range(len(li)):
    flag=True
    for j in range(i+1,len(li)):
        # if(i==skip):
        #     flag=False
        #     continue
        if(li[i]==li[j] ):
            li.pop(i)
            skip=j
            flag=False
            break
    if(flag == True):
        op=li[i]
        break

print(op)