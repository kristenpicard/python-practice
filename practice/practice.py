
def min(a, b):
    if a > b:
        return b
    elif b > a:
        return a
    else:
        return a
    
print(min(2, 2))

def max(a, b):
    if a >= b:
        return a
    elif b > a:
        return b


def test1(a,b,c):
    if a == b:
        print("a is equal to b")
    elif b == c:
        print("a is not equal to b, but b is equal to c")


def test2(a,b,c):
    if a == b:
        print("a is equal to b")
    if b == c:
        print("a is not equal to b, but b is equal to c")

print(min(1,max(5,min(35,5.986))))
