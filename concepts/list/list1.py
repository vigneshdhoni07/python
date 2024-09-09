# list declearation 
a=[3,4,5,"vignesh",True,5.8]
print(a)
print(type(a))

# access a list
print(a[1])
# print(a[10]) error list out of range

# modify list
a[1]=10
print(a)

#slicing list
print(a[1:4])#starts from index 1 and stops at 3
print(a[1:])#starts from index 1 and goes till last
print(a[:])#enitre list
print(a[:4])#starts from 0 goes till 3

#inserting element
b=[10,11,12]
b.append(13)#insert element at last of list
print(b)
b.insert(1,14)# insert element at first index and appends all other element
print(b)
b.insert(10,15)# inserts element at last if index is not in list
print(b)
b.append([1,2,3])# inserts another list at end
print(b)
b.extend([4,5,6])# inserts [4,5,6] as elements at end
print(b)

#removing element
c=[1,2,3,1,2,20,6]
c.remove(20)#removes element 20
print(c)
c.remove(1)#removes element 1 which matches first
print(c)
# c.remove(45)# error as 45 is not present

c.pop()# removes last element in list
print(c)
c.pop(2)# removes element with index 2
print(c)
# c.pop(7)# error pop index out of range

#length 0f list
print(len(c))