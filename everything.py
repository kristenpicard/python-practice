# variables (number, strings, booleans(i.e. True/False))
# if/else = control flow or basic if-else logic.
# functions, are reusable templates of code. Also somtimes called subroutines.
# for/while loops are loops/iterations of pieces of code.
# classes encapsolate variables (data) and functions
    # variables in a class are called class members, or attributes
    # functions in a class are called class methods

# variables
a = 1 # this is number assigned to a variable
b = 'string' #this is a string assigned to a variable
c = True # this is a boolean assigned to a variable
d = b # this is a variable assigned to another variable
listOfNumbers = [1,2,3,4,5] #this is a list of numbers assigned to a variable


# loops

# this is a 'for' loop
mylist = [1,2,3,4,5]
for column in mylist:
    print(mylist) 

# this is a 'while' loop
stopValue = 0
while (stopValue < 10):
    print(stopValue)
    stopValue = stopValue + 1


#functions & if/else statements

# function defintions
def add(a, p):
   c = a + p 
   return c

def sub(a, b):
   c = a - b 
   return c

#using the function definitions
b = add(1,2)
e = sub(8,5)
f = add(b,e)
g = sub(5,f)

# function definitions with if/else
def X(a):
    t = a +1
    b = t/3
    #control flow
    if b>5:
        return True
    if b<5:
        return False
    else:
        return 'a and b are equal'
y = X(3)    
print(y)




# recursive function
def fib(a,b):
    print(a,b)    
    if(b > 2000):
        return b
    return fib(b, a+b)

print(fib(0, 1))





#classes

# class definitions
class Cat:
    # members/attributes
    fur = True
    tail = True
    legs = 4
    ears = 'pointy'

    #methods
    def eats(self, meat):
        return 'the cat ate ' + meat

    def meow(self):
        return 'meow!' 

    def sleep(self):
        return 'zzzz'

    def lick(self):
        return 'slurp'


class MeatFreezer:
    steak = 'steak'
    ham = 'ham'
    chicken = 'chik'
    tuna = 'tuna'

    def getSteak(self, a):
        return self.steak + ' ' + a

    def getChicken(self):
        return self.chicken

    def getHam(self):
        return self.ham

    def giveTuna(self):
        return self.tuna

class Seasoning:
    pepper = 'pepper'
    salt = 'salt'
    garlic = 'garlic'

    def getPepper(self):
        return self.pepper

    def getSalt(self):
        return self.salt

    def getGarlic(self):
        return self.garlic

# using classes

# this creates an object by instantiating a class 
ronsCat = Cat()
kristensCat = Cat()
meatFreezer = MeatFreezer()
seasoning = Seasoning()
print(ronsCat.eats(meatFreezer.getSteak(seasoning.getSalt())))