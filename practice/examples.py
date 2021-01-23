# primative data types: number, boolean, strings
# complex data types are objects

# string
cat = "cat"

# string
dog = "dog"

# string
animal = dog

# key/value pair
# list of strings
list1 = [cat, dog, animal]

# string
myAnimal = list1[1]

# string
myAnimal2 = list1[2]

# boolean
test = True

# boolean
test2 = False

# list (contains type strings and a boolean)
list1.append(test)

if animal == cat:
    print(cat)
elif animal == dog:
    print(dog)
else: 
    print("nothing")


# ==, >, <, >=, <=, !=
if list1[2] == dog:
    print("hello")
    if list1[0] == cat:
        print("goodbye")
    else:
        print("it will never get here")


def min(a, b, c):
    if a >= b and c >= b:
        return b
    elif b > a and c > a:
        return a
    elif a > c and b > c:
        return c


print(min(1,2,3))