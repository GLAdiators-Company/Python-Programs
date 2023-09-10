class Employee:
    company = 'Apple'
    def __init__(self,name):
        self._name = name

    def name(self):
        return self._name

    def name(self,name):
        self._name = name
    def show(self):
        print(f'Your name is {self._name} and company is {self.company}')

    @classmethod
    def changeCompany(cls,cname):
        cls.company = cname

e1 = Employee('Harry')
e1.name = 'Yash'
e1.show()
print(e1.company)
e1.changeCompany('Hero Honda')
print(e1.company)
print(Employee.company)