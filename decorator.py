def greet(fx):
    def mfx(*args,**kwargs):
        print('Good morning')
        fx(*args,**kwargs)
        print('Good bye')
    return mfx

@greet
def hello():
    print('Hello world')

@greet
def add(a,b):
    print(a+b)

hello()
add(1,2)