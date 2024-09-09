class Bank:
    def __init__(self,deposit,acNo) -> None:
        self.deposit=deposit
        self.acNo=acNo
        
class Savings(Bank):
    def __init__(self, deposit, acNo,interest) -> None:
        Bank.__init__(self,deposit, acNo)
        self.interest=interest
        
class CreditCard(Bank):
    def __init__(self, deposit, acNo,credit) -> None:
        Bank.__init__(self,deposit, acNo)
        self.credit=credit
        

class Student(Savings,CreditCard):
    def __init__(self, deposit, acNo, interest, credit) -> None:
        Savings.__init__(self,deposit,acNo,interest)
        CreditCard.__init__(self,deposit,acNo,credit)
        



sa=Savings('100000','ACo03242','10%')
print('Saving',sa.__dict__)
cc=CreditCard('10000','AC83993','5000')
print('Credit Card',cc.__dict__)
s=Student('100000','UE90230','10%','50000')
print('Student',s.__dict__)