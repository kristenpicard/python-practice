def reverseList(a):
    # make a copy of a and assigned it to b
    # b is equal to [1,2,3,4,5]
    b = a[:]
    # find the length a, which is also the length of b
    # this is the number of elements in the list
    # this becomes equal to 5
    lengthOfA = len(a)
    # for{i = 0; i < lenghtOfA; i++}
    i = 0
    while(i < lengthOfA):
        # variable in list at spot 4 is assigned the value of variable in list a at spot 0
        b[lengthOfA-1-i] = a[i]
        i = i + 1
        
    # return full list
    return b

myList = [1,2,3,4,5]
myListReversed = reverseList(myList)
print(myListReversed)

