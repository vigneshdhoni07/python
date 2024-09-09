class Person:
    salary=10000
    def  __init__(self,name,age) :
        self.name=name
        self.age=age
        
    def dispName(self):
        print("Name",self.name)
        

class Animal:
    def __init__(self,name,color) :
        self.name=name
        self.color=color
    def display(self):
        print(Person.salary)

# vignesh=Person("Vignesh",29)

# vignesh.dispName()
# print('Age',vignesh.age)
# print(Person.salary)

animal=Animal('Cat','White')
print(animal.__dict__)
animal.color='Blue'
print(animal.__dict__)
