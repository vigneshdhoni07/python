print("Enter Number")
n=int(input())
#   1   
#  121
# 12321
#1234321
i=1
while (i<=n):
    j=1
    p=1
    k=i-1
    while(j<=2*n-1):
        if(j>=n-i+1 and j<n+1):
            print(p,end="")
            p+=1
        elif(j>n):
            
            if(k>0):
            
              print(k,end="") 
              k-=1
            else:
              print(" ",end="")
                
        else:
            print(" ",end="")
        
      
        j+=1
    print()
    i+=1
print()
############################################################################
#   *
#  ***
# *****
#*******
i=1
while (i<=n):
    j=1
    p=1
    k=i-1
    while(j<=2*n-1):
        if(j>=n-i+1 and j<n+1):
            print("*",end="")
            p+=1
        elif(j>n):
            
            if(k>0):
            
              print("*",end="") 
              k-=1
            else:
              print(" ",end="")
                
        else:
            print(" ",end="")
        
      
        j+=1
    print()
    i+=1

print()

############################################################################
#   1
#  232
# 34543
#4567654
i=1
while (i<=n):
    j=1
    p=i
    k=i-1
    while(j<=2*n-1):
        if(j>=n-i+1 and j<n+1):
            print(p,end="")
            p+=1
        elif(j>n):
            
            if(k>0):
              p-=1
              print(p-1,end="") 
              k-=1
            else:
              print(" ",end="")
                
        else:
            print(" ",end="")
        
      
        j+=1
    print()
    i+=1

print()
#############################################################################
#  *  
# ***
#*****
# ***
#  *
i=1
s=n//2+1
e=n//2+1

while (i<=n):
   j=1
   while(j<=n):
      
        if(j>=s and j<=e):
           
           print("*",end="")
        else:
           print(" ",end="")
        j+=1
   if(i<n//2+1):
    s-=1
    e+=1
   
   else:
    s+=1
    e-=1
    
    
   print()
   i+=1
print()

############################################################################
#    1
#   212
#  32123
# 4321234
#543212345
i=1
while (i<=n):
    j=1
    p=i
    k=i-1
    l=2
    while(j<=2*n-1):
        if(j>=n-i+1 and j<n+1):
            print(p,end="")
            p-=1
        elif(j>n):
            
            if(k>0):
              
              print(l,end="") 
              l+=1
              k-=1
            else:
              print(" ",end="")
                
        else:
            print(" ",end="")
        
      
        j+=1
    print()
    i+=1

print()
##################################################################################
#*
# * *
#  * * *
# * *
#*

i=1
s=1
e=1

while (i<=n):
   j=1
   while(j<=n):
      
        if(j<=e and j>=s):
           
           print("*",end=" ")
        else:
           print(" ",end="")
        j+=1
   if(i<n//2+1):
    e+=2
    s+=1
   
   else:
    e-=2
    s-=1
    
    
   print()
   i+=1
print()
########################################################################################
#1      1
#12    21
#123  321
#12344321

i=1


while (i<=n):
   j=1
   p=i
   while(j<=2*n):
      
        if( j<=i):
           
           print(j,end="")
        elif(j>2*n-i):           
            print(p,end="")
            p-=1
        else:
           print(" ",end="")
        j+=1
 
    
    
   print()
   i+=1
print()

#################################################################################
#*000*000*
#0*00*00*0
#00*0*0*00
#000***000


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

