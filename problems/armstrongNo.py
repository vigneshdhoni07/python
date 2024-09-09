print("Enter No")
n=int(input())

def lengthOfNo(x):
    c=0
    while(x>0):
       x=x//10
       c+=1
    return c

def armstrongNo(y):
    a=y
    k=0
    p=lengthOfNo(y)
    while(y>0):
        z=y%10
        b=z**p
        k+=b
        y=y//10
    if(a==k):
        return "true"
    else:
        return "false"

print(armstrongNo(n))