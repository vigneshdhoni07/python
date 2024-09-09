class Animal:
    _name=None
    _weight=None
    _color="Brown"
    def __init__(self,name,weight) :
        self._name=name
        self._weight=weight
        
    def dispDetails(self):
        print('Name',self._name)
        
class Cat(Animal):
    _height=None
    def __init__(self, name, weight,height):
        super().__init__(name, weight)
        self._height=height

  

c=Cat("Cat",10,5)
print(c._name)
print(c._height)
print(Animal._color)
print(c.__dict__)
c._name='Lion'
print(c.__dict__)


