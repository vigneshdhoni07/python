#square pattern of characters
print("Enter N")
n=int(input())
print("Enter C")
c=input()
#abcd
#abcd
#abcd
#abcd
k=ord(c)
i=1
while (i<=n):
    p=k
    j=1
    while(j<=n):
        print(chr(p),end="")
        j+=1
        p+=1

    print()
    i+=1
print()
#######################################################################################
#abcd
#bcde
#cdef
#defg
i=1
while (i<=n):
    p=ord(chr(k+i-1))
    j=1
    while(j<=n):
        print(chr(p),end="")
        j+=1
        p+=1

    print()
    i+=1
print()
#######################################################################################
#a
#bc
#cde
#defg
#efghi

i=1
while (i<=n):
    p=ord(chr(k+i-1))
    j=1
    while(j<=i):
        print(chr(p),end="")
        j+=1
        p+=1

    print()
    i+=1
print()