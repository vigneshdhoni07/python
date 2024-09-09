import time 
def pow(x,n):
    op=x
    if(n==0):
        return 1
    while(n>1):
        op=x*op
        n=n-1
    return op
# print(time.time())
# print(pow(2,0))
# print(pow(2,1))
# print(pow(2,2))
# print(pow(2,3))
# print(pow(2,4))

def powRecursive(x,n):
    if(n==0):
        return 1
    return x*powRecursive(x,n-1)

# print(powRecursive(2,0))
# print(powRecursive(2,1))
# print(powRecursive(2,2))
# print(powRecursive(2,3))
a=time.time()
print(powRecursive(2,200))
b=time.time()
print('time taken r1',b-a)
# Optimised Solution
def powRecursive2(x,n):
    if(n==0):
        return 1
    if(n==1):
        return x

    a= powRecursive2(x,n//2)
    if(n%2==0):
     return a*a
    else:
        return a*a*x

print('----------------------------------------------------------------------')
c=time.time()
print(powRecursive2(2,0))
d=time.time()
print('time taken r2',d-c)
# print(powRecursive2(2,1))