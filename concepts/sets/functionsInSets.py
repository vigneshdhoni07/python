a={1,2,3,4}
b={3,4,5,6}
c={3,4}
d={7,8}

print(a.intersection(b)) #{3,4}
print(a.union(b)) #{1,2,3,4,5,6}
print(a.difference(b))#{1,2}
print(b.difference(a))#{5,6}
print(a.symmetric_difference(b))#{1,2,5,6}
a.symmetric_difference_update(b)
print(a)#{1,2,5,6}
a={1,2,3,4}
a.intersection_update(b)
print(a)#{3,4}
a={1,2,3,4}
a.difference_update(b)
print(a)
a={1,2,3,4}
print(a.issubset(b)) # False
print(c.issubset(a)) # True
print(a.issuperset(c)) # True
print(a.isdisjoint(d)) # True
print(a.isdisjoint(c)) # False