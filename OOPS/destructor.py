class Computer:
    def __init__(self) -> None:
        self.name='Computer'
        print('Computer Created')
        
    def __del__(self):
        print("Computer is Destroyed")
        
c=Computer()
print(c.__dict__)
print(id(c))
