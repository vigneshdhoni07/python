class User:
    def __init__(self,name,email) -> None:
        self.name=name
        self.email=email
        
class Customer(User):
    def __init__(self, name, email,cart) -> None:
        super().__init__(name, email)
        self.cart=cart
    
class PremiumCustomer(Customer):
    def __init__(self, name, email, cart,discount) -> None:
        super().__init__(name, email, cart)
        self.discount=discount
        

u=User('Vignesh','Vigneshr470@gmail.com')
c=Customer('Virat','Virat@gmail.com',10)
p=PremiumCustomer('Dhoni','Dhoni@gmail.com',25,0.1)

print(u.__dict__)
print(c.__dict__)
print(p.__dict__)
