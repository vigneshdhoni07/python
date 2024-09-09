print("Enter N")
n=int(input())
# ****
# ***
# **
# *
i=1
while (i<=n):
    j=1
    while(j<=n):
        if(j>=n-i+1):
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    print()
    i+=1
print()

##################################################################################
#   1
#  12
# 123
#1234

i=1
while (i<=n):
    j=1
    p=1
    while(j<=n):
        if(j>=n-i+1):
            print(p,end="")
            p+=1
        else:
            print(" ",end="")
        j+=1
        
    print()
    i+=1
print()


i=1
while (i<=n):
    j=1
    p=1
    while(j<=n):
        if(j>=n-i+1):
            print(p,end="")
            p+=1
        else:
            print(" ",end="")
        
      
        j+=1
    print()
    i+=1
print()