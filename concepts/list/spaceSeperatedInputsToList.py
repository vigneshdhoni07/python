print("Enter List")
# n=int(input())
str=input()
str_split=str.split(" ")
li=[]
for i in str_split:
    li.append(int(i))

print(li)
#or
la=[int (x) for x in input().split()]
print(la)