n=input("Enter String:")

# def replacepi(n,i,l,s):
#     if(i>=l-1):
#         return s
#     if(n[i]=="p" and n[i+1]=="i"):
#         s+="3.14"
#         return replacepi(n,i+2,l,s)
#     else:
#         s+=n[i]
#         return replacepi(n,i+1,l,s)
    
# print(replacepi(n,0,len(n),""))

def replacepi2(n):
    if(len(n)<=1):
        return n
    if(n[0]=="p" and n[1]=="i"):
        op="3.14"+ replacepi2(n[2:])
        return op
    else:
         op=n[0]+ replacepi2(n[1:])
         return op
    
print(replacepi2(n))