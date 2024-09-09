class Vehicle:
    def EngineStart(self):
        print('Engine Started')
        
class Bike(Vehicle):
    def __init__(self,brake,gas) -> None:
        super().__init__()
        self.brake=brake
        self.gas=gas
        
class Car(Vehicle):
    def __init__(self,AC,AirBags) -> None:
        super().__init__()
        self.AC=AC
        self.AirBags=AirBags
        
b=Bike('Disc','Petrol')
c=Car('All Weather AC',4)

print(b.__dict__)
print(c.__dict__)
b.EngineStart()
c.EngineStart()