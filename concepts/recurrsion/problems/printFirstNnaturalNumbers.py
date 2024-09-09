n=int(input("Enter Number:"))

def printN(n):
    if(n==-1):
        return 
    printN(n-1)
    print(n)
    return

printN(n)