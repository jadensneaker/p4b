#local scope 
def add():
    x=10 #local variables
    y=20
    z=x+y
    return z

print(add())

counter = 5 

def addNumber(x):
    global counter 

    counter = counter * x 
    return counter 

print(addNumber(5))
print(addNumber(5))

