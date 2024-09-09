print("Enter Number")
n=int(input())

for i in range(1,n+1,1):
    for j in range(n,0,-1):
        if(i==j):
         print("*",end="")
        else:
         print(j,end="")

    print()
print()
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if(j<=i-1):
         print(" ",end="")
        else:
         print("*",end="")

    print()

def gcd (x,y):
   
   if(x<y):
      min=x
      diff=y-x
   else:
      min=y
      diff=x-y
   for i in range(min,0,-diff):
      if(x%i==0 and y%i==0):
         return i
      
print(gcd(12,18))      