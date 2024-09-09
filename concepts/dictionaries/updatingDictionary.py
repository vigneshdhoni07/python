a={"name":"vignesh","age":29,"salary":10000}
print(a)
a["weight"]=80 #adding new key
a["age"]=30 #updating existing key
print(a)
b={"name":"virat","height":"5"}
a.update(b) # change keys of according to keys of b if exists or adds new key in a
print(a)
c=a.pop("name")# removes and returns the key
print(c)
# a.pop("name") # Error as the key does not exist
del a["age"] # another way of deleting key
print(a)
# del a["age"] # Error as key doesn't exist
a.clear() # clears eniter dictionary
print(a)
del a # deletes dictionary
# print(a)
