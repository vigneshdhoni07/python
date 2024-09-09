str="Welcome to Coding Ninjas"
str2=""
str3=""
for i in range(len(str)-1,-1,-1):
    if(str[i]==" " or i==0):
        str2+=str[i]
        str3=str2+str3
        str2=""
    str2+=str[i]
