class Product:
    def __init__(self,description) -> None:
        self.description=description
    def printDescription(self):
        print(self.description)
        
class LightWeightProduct(Product):
    def __init__(self,weight,description):
        self.weight=weight
        super().__init__(description)
        
    def printWeight(self):
        print(self.weight)
        
lwp=LightWeightProduct(5,"This is a computer")
lwp.printWeight()
lwp.printDescription()
print(dir(lwp))