square = lambda x : x**2
list1 = [1,2,3,4,5,6]
list1 = list(map(square,list1)) #It is used to map a funciton with a variable 
print(list1)


fun_greater = lambda x: x>10
newList = list(filter(fun_greater,list1)) # It is a function to filter out values from a given sequence of list
print(newList)

from functools import reduce
numbers = [1,2,3,4,5,6]
mul = lambda x,y : x*y
multi = reduce(mul,numbers)
print(multi) 