class Product:
    count = 0
    def __init__(self,name,price) -> None:
        self.name=name
        self.price=price
    @staticmethod    
    def printDiscount(price,discount):
        print(price*discount)
        
Product.printDiscount(10000,0.15)# calling it directly with class name
p=Product('HeadPhones',2500)
p.printDiscount(20000,0.2)# calling by creating instance