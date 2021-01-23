
# if/else = control flow or basic if-else logic.
# functions, are reusable templates of code. Also somtimes called subroutines.
# for/while loops are loops/iterations of pieces of code.


# classes encapsolate variables (data) and functions
# variables in a class are called class members
# functions in a class are called class methods
class Cat:
    fur = True
    tail = True
    legs = 4
    ears = 'pointy'

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

# this creates an object by instantiating a class 
ronsCat = Cat()
kristensCat = Cat()
meatFreezer = MeatFreezer()
seasoning = Seasoning()
print(ronsCat.eats(meatFreezer.getSteak(seasoning.getSalt())))
