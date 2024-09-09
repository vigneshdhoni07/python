import sys
# sys.setrecursionlimit(2000)
n=int(input("Enter Number:"))

def factorial(n):
    if(n==0):
        return 1
    return n*factorial(n-1)

print(factorial(n))