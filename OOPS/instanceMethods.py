class Product:
    __company='Sony'
    def __init__(self,name,price) -> None:
        self.name=name
        self.price=price
        
    def details(self):
        print(self.name)
        

p=Product('Phone',50000)

p.details()