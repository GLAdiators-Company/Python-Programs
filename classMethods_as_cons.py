class Employee:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls,string):
        return cls(string.split('-')[0],string.split('-')[1])
string1 = 'Yash-69000'
e1 = Employee.from_string(string1)
print(id(e1))
print(id(Employee))