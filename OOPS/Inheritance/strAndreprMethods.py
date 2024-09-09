class Sea:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
        

    
s=Sea('JellyFish',25)

# without __str__ and __repr__ methods
print('without __str__ and __repr__ methods')
print(s)
print(str(s))
print(repr(s))

class Ocean:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
        
    def __str__(self) -> str:
        return f'This Ocean creature is {self.name} and age is {self.age}'
    
    def __repr__(self) -> str:
        return f'Ocean(\'{self.name}\',{self.age})'
    
o=Ocean('Shark',35)

# with __str__ and __repr__ methods
print('with __str__ and __repr__ methods')
print(o)
print(str(o))
print(repr(o))