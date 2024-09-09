print("Enter Number")
n=int(input())
b=True
if(n==2):
    print("Prime")
elif(n%2==0 and n>2):
    print("Not a Prime")
else:
    for i in range(3,n,2):
        if(n%i==0):
            b=False    
    if(b):
        print("Prime")
    else:
        print("Not Prime")        