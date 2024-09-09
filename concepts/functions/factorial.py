print("Enter The Number")
n=(int(input()))

def fact(x):
    ans=1
    for i in range(1,x+1):
        ans*=i
    return ans

print(fact(n))