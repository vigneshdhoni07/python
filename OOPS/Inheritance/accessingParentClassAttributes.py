class Product:
    def __init__(self,price,discount) -> None:
        self.__price=price
        self.discount=discount
        
    def getPrice(self):
        return self.__price
    def getDiscount(self):
        return self.discount
    def calculatePrice(self):
        return self.__price-self.__price*self.discount
class LightWeightProduct(Product):
    def getPrice(self):
        # print(dir(self))
        # return self.__price #gives error because accessing private variables of parent class
        # return self._Product__price # way to access private variables of parent class
        return (super().getPrice()) # correct way of accessing private variablex    
    def getDiscount(self):
        return self.discount # accessing public attributes of parent class
    def calculatePrice(self):
        self.discount=self.discount+0.10 # giving additional discount for light weight products
        return super().calculatePrice()
lwp=LightWeightProduct(1000,0.2)
print(lwp.getPrice())
print(lwp.getDiscount())
print(lwp.calculatePrice())