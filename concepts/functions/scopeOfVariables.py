a=10
def B():
    b=20
    print(a) #10
    print(b) #20
    print(c) #30 c is defined after fn but before fn call
    # print(d) error as d is not defined while fn call
# print(b)  error as we are accessing b outside fn block
print(a) #10
c=30
# B()
d=40

e=60
def E():
    e=70
    print(e)
    print(id(e))
print(e)
E()
print(e)
print(id(e))

f=80
def F():
    global f
    f=90
    print(f)
    print(id(f))
print(f)
F()
print(f)
print(id(f))