# Generators in python are special functions whicha are used to iterate over a sequence to generate on-the-fly value
# They helps to save memory 
def my_generator():
    for i in range(10):
        yield i     #We can create a gen using "yield" keyword

gen = my_generator()
print(next(gen))  #Using next keyword to access the element 
print(next(gen))
print(next(gen))
print(next(gen))



