a=(1,2,3)
b=4,5,6
# for loop
for i in a:
    print(i)

# Boolean
print(1 in a)
print(4 in a)

# Length
print(len(a))

# concatinating two tuples
c=a+b
print(c)

# tuple of tuples
d=(a,b)
print(d)

# repitition
e=a*4
print(e)

# min max functions
print(min(a))
print(max(a))
f=1,2,"d",4
# print(min(f)) run time error as f contains non numerical values but if all elements are string it will work
g=1,2.2
print(max(g))

# converting list to tuple
l=[1,2,3,4,5]
t=tuple(l)
print(t)

q="ab","abc","def"
print(min(q))