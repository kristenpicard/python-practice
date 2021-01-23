import random 

def randomListGenerator():
    i = 0
    myList = [] 
    while(i<10):
        myList.append(random.random())
        i = i + 1
    return myList


def min(aList):
    i = 0
    while(i < len(aList)):
        if i == 0:
            smallestNumber = aList[i]
        elif aList[i] < smallestNumber:
            smallestNumber = aList[i]
        i = i + 1


    return smallestNumber


myList = randomListGenerator()
output = min(myList)
print(myList)
print(output)