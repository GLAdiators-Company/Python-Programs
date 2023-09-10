class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender        
        

p = Person('Yash',18,'M')
print(p.__dict__)
print(type(p.__dict__))

print(dir(p))

print()
print()
print(help(p))
