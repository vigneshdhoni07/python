class Phone:
    def make_Call(self):
        print('Calling.........')
        
    def send_SMS(self):
        print('Sending SMS')
        
class Computer:
    def browse_Internet(self):
        print('Internet Surfing')
        
    def send_email(self):
        print('Sending Email')
        
class SmartPhone(Phone,Computer):
    def __init__(self,model,year) -> None:
        super().__init__()
        self.model=model
        self.year=year
        

smartPhone=SmartPhone('OnePlus 11r',2023)

smartPhone.browse_Internet()
smartPhone.make_Call()