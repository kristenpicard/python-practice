# variables
a = 1
b = 'string'
c = b


# loops

mylist = [1,2,3,4,5]
for column in mylist:
    print(mylist) 

stopValue = 0
while (stopValue < 10):
    print(stopValue)
    stopValue = stopValue + 1

#functions

def add(a, p):
   c = a + p 
   return c
   
print(c)

def sub(a, b):
   c = a - b 
   return c
   
print(c)

b = add(1,2)
e = sub(8,5)
f = add(b,e)
g = sub(5,f)

def X(a):
    t = a +1
    b = t/3
    if b>5:
        return True
    if b>5:
        return False
y = X(3)    
print(y)

#classes