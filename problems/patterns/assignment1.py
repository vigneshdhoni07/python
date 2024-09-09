print("Enter N")
#1111
#000
#11
#0
n=int(input())

for i in range(1,n+1,1):
    for j in range(n,i-1,-1):
        if(i%2==0):
         print("0",end="")
        else:
         print("1",end="")
    print()
print()

#######################################################################################
#1234
# 234
#  34
#   4
#  34
# 234
#1234
for i in range(1,2*n,1):
    if(i<=n):
     for s in range(0,i-1,1):
        print(" ",end="")
     for j in range(i,n+1,1):
        print(j,end="")
    else:
        for d in range(0,2*n-i-1,1):
         print(" ",end="")
        for k in range(2*n-i,n+1,1):
         print(k,end="")
    
    print()
print()
############################################################################################
#  *
# ***
#*****
# ***
#  *
for i in range(1,n+1,1):
    if(i<=n//2+1):
     for s in range(0,n//2+1-i,1):
        print(" ",end="")
     for j in range(1,2*i,1):
        print("*",end="")
    else:
        for s in range(0,i-n//2-1,1):
         print(" ",end="")
        for j in range(1,2*(n-i)+2,1):
         print("*",end="")
  
    
    print()
print()
###########################################################################################
#555555555
#544444445
#543333345
#543222345
#543212345
#543222345
#543333345
#544444445
#555555555
for i in range(1,2*n,1):
    if(i==1 or i==2*n-1):
       for t in range(1,2*n,1):
        print(n,end="")
    elif(i<n+1):
   
     for f in range(1,i,1):
        print((n-f+1),end="")
     for s in range(i+1,2*n-i+2,1):
        print((n-i+1),end="")
     for t in range(i,1,-1):
        print((n-t+2),end="")      
    else:
        
        for F in range(1,2*n-i+1,1):
           print(n-F+1,end="")
        for S in range(1,(i-n+1)*2-1,1):
           print(i-n+1,end="") 
        for T in range(1,2*n-i,1):
           print(i-n+T+1,end="")      
      
  
    
    print()
print()
###############################################################################################

for i in range(1,n+1,1):

    k=(2*(i-1)*n)+1
    l=(2*(n-i)+1)*n+1
    if(i<=n//2):
    
     for j in range(1,n+1,1):
        print(k,end=" ")
        k+=1
    elif(i==n//2+1):
       for s in range((n-1)*n+1,n*n+1,1):
          print(s,end=" ")
       print
    else:
       
       for u in range(1,n+1,1):
         print(l,end=" ")
         l+=1
    
    print()