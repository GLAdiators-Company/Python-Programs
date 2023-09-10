class Person:
    
    def __init__(self,value):
        self._value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self,value):
        self._value = value
    
yash = Person(18)
yash.value = 100
print(yash.value)