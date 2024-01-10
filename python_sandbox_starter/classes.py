# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Constructor : a function that runs when you instantiate an object from a class
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    def has_birthday(self):
        self.age += 1

# Extend user class to new class
class Customer(User):
        # Constructor : a function that runs when you instantiate an object from a class
    def __init__(self, name, email, age, balance):
        self.name = name
        self.email = email
        self.age = age
        self.balance = balance

    def set_balance(self, balance):
        self.balance = balance    
        
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

# Init user object
me = User('Madeleine Beatty', 'madeleine@gmail.com', 36)
# print(type(me))
print(me.name)

print(me.greeting())

me.has_birthday()
print(me.greeting())

# initialize customer object
thilly = Customer('thilly t.', 'thilly@gmail.com', 11, 0)
thilly.set_balance(120)
print(thilly.greeting())



