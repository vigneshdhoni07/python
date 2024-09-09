class Bank:
    def __init__(self,balance):
        self.__balance=balance
    
    def withDraw(self,amount):
        if(amount<self.__balance):
            self.__balance-=amount
            print("Amount With Drawn")
        else:
            print("Amount Cannot be with drawn")
            
    def checkBalance(self):
        print('Balance :',self.__balance)
        
b1=Bank(25000)
b1.checkBalance()
b1.withDraw(15000)
b1.checkBalance()
b1.__balance=30000# can not change the balance as it is private
b1.checkBalance()
b1._Bank__balance=50000 # this way we can change the balance even it is private
b1.checkBalance()

        