class Vehicle:
    def __init__(self,speed,torque) -> None:
        self.speed=speed
        self.torque=torque
        
    def getSpecs(self):
        return f'Speed is {self.speed} and Torque is {self.torque}'

class Car(Vehicle):
    
    def __init__(self, speed, torque,wheels) -> None:
        # Vehicle.__init__(self,speed, torque)
        super().__init__(speed,torque)
        self.wheels=wheels
        
    def getSpecs(self):
        return f'{super().getSpecs()} No.of wheels {self.wheels}'
    

c=Car(100,100,4)

print(c.getSpecs())