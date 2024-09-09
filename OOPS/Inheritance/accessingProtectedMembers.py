class Product:
    def __init__(self,description) -> None:
        self._description=description
        
    def getDescriptionBase(self):
        return self._description
    
class LightWeightProduct(Product):
    def __init__(self,description) -> None:
        super().__init__(description)
        
    def getDescriptionDerived(self):
        return self._description
    
#correct way of accessing 
p=Product('Mobile')
l=LightWeightProduct('Tablet')

print(p.getDescriptionBase())
print(l.getDescriptionDerived())

#incorrect way 
print(p._description)
print(l._description)