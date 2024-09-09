a={"apple",23,"apple"}
print(a)# {"apple",23}
# print(a[0]) # Error
# print(a["apple"]) # Error
print("apple" in a)# True
print(25 in a)# False

for v in a:
    print(v)

a.add("orange")
a.add("orange")
print(a)

b={23,"grape"}
a.update(b)
print(a)

a.remove("grape")# removes grape
print(a)
# a.remove("grape") # KeyError
a.discard(23)# discards 23
print(a)
a.discard(23)# No error
a.add("orange")
a.add("pineapple")
a.add("Grape")
print(a)
a.pop()
print(a)
