def square(n):
    return n*n

s=square # storing function in variable
print(s(5))

def cube(s,n): # passing function as argument
    op=s(n)*n
    return op

print(cube(s,5))
    
def factors(s): # Nested Methods or function returning a function
    def inner(n):
        a=s(n)
        op=[]
        for i in range(2,a):
            if(a%i==0):
                op.append(i)
        return op        
    return inner

out=factors(s)
print('factors of 10 square',out(10))