def min(a):
    i = 0
    smallest = 0
    # while 'i' is less than the number of elements in the list
    while(i < len(a)):
        # first time the first element is the smalled so just grap it
        if(i == 0):
            # b equals the element of the list 'a' at index 'i'
            smallest = a[i]
        else:
            # if current element is less than previously found smallest)
            if(a[i] < smallest):
                # replace the previously smalled element with this element, since its smaller
                smallest = a[i]
        
        # increment the index/number 'i' by 1
        i = i + 1

    return smallest

print(min([7467,82,7398,59]))