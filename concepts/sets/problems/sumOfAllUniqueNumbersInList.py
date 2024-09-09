a=[1,2,3,4,5,4,3,2]
# b={0}
b=set()
for i in a:
    b.add(i)

s=0
for j in b:
    s+=j
    
print(s)