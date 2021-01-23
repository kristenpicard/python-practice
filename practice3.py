def min(someList):
    i = 0
    while(i < len(someList)):
        if i == 0:
            smallestNumber = someList[i]
        elif smallestNumber > someList[i]:
            smallestNumber = someList[i]
        i = i + 1

    return smallestNumber

myList = [5, 9, 4, 8]
print(min(myList))