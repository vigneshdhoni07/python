def nat(n):
    if n==1:
        return 1
    return n+nat(n-1)

n=int(input("Enter Number:"))
print(nat(n))