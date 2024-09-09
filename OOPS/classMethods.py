class Employee:
    __company='Coding Ninjas'
    def __init__(self,name,id) -> None:
        self.name=name
        self.id=id
    @staticmethod    
    def greet():
        return 'Have a nice day'
    @classmethod
    def intro(cls):
        return 'welcome to '+cls.__company+'.'+cls.greet() 
    
e=Employee('Vignesh',1001)

print(Employee.intro())