s="Good Morning"
l=len(s)
def replaceStr(s,a,b,i,l,n):
    if(i==l):
        return n
    if(s[i]==a):
        n+=b
    else:
        n+=s[i]
    return replaceStr(s,a,b,i+1,l,n)       

print(replaceStr(s,"o","c",0,l,""))
