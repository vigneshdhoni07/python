li=[1,2,3,4,5,6,7]
for i in range(len(li)//2):
    li[i],li[len(li)-1-i]=li[len(li)-1-i],li[i]

print(li)

print("********************************************")
print("******Using Negative Index******************")

li=[1,2,3,4,5,6,7]
for i in range(len(li)//2):
    li[i],li[-i-1]=li[-i-1],li[i]

print(li)

print("********************************************")
print("******Using List Sequence******************")

li=[1,2,3,4,5,6,7]
li=li[::-1]

print(li)