def recursion(n):
    if(n==0):
        return
    print(n)
    return recursion(n-1)

recursion(5)