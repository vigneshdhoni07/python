from datetime import datetime

def cube(s):
    def inner(n):
        op=s(n)*n
        return op
    return inner




@cube
def square(n):
    return n*n

s=square

# special_decorator=cube(s) # one way of adding decorator
# print(special_decorator(10))

# other way of adding decorator is using @ before base function

print(square(5))

def logDate(func):
    def wrapper():
        print(f'Function: {func.__name__}\nRun On: {datetime.today().strftime("%H:%M:%S")} ')
        print(f'{"-"*30}')
        func()
    return wrapper
@logDate
def dailyBackup():
    print('Daily Backup ran successfully')
    
dailyBackup()