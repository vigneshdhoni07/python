print("Enter N")
n=int(input())

i=1

s=1
e=2*n+1
while (i<=n):
   j=1
   p=i
   while(j<=2*n+1):
        if(j==n+1 or j==s or j==e):
            print("*",end="")
        else:   
            print("0",end="")
        j+=1
   s+=1
   e-=1
   print()
   i+=1
print()
