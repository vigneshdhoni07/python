class Animal:
    __name=None
    __color=None
    def __init__(self,name,color):
        self.__name=name
        self.__color=color
    
    def __dispDetails(self):
        print('Name',self.__name)
        print('Color',self.__color)
        
    def AccessPrivateFnOutsideClass(self):
        self.__dispDetails()
        

animal=Animal('Lion','Brown')
# print(Animal.__name) Error
# print(animal.__name) Error
animal.AccessPrivateFnOutsideClass()