a={
    "name":"vignesh",
    "age":29
    }

print(a)
# other ways of creating dictionary

# using copy method
b=a.copy()
print(b)

# using dict keyword
c=dict([("a","b"),(1,2)])
print(c)

# using dict.fromKeys
d=dict.fromkeys(["c","d","e"])
e=dict.fromkeys(["f","g","h"],5)

print(d)
print(e)