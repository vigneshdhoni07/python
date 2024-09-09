# *c represents variable length tuple
# variable length input
def sum(a,b,*c):
    ans=a+b
    for i in c:
        ans+=i
    return ans

print(sum(1,2,3))
print(sum(1,2,3,4,5))
print(sum(1,2))

# variable length output function
def sum_diff(a,b):
    return a+b,a-b

print(sum_diff(5,2))
c,d=sum_diff(8,3) # length of tuple returned by function should be same as destructuring elements
print(c)
print(d)
    