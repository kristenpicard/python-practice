
# input = deck
def shuffle(deck):

    # find size of half deck
    sizeOfDeck = len(deck)
    halfway = int(sizeOfDeck/2)

    # split deck
    list1 = deck[0:halfway]
    list2 = deck[halfway:sizeOfDeck]
   
    # complete shuffle
    shuffle1 = list()
    numberList = range(0, halfway)
    for number in numberList:
        shuffle1.append(list1[number])
        shuffle1.append(list2[number])        

    # output    
    return shuffle1


# set the size of the deck
deckSize = 5000

# make a deck 1 .. N
cards = list(range(1, deckSize+1))

# initialize the number of shuffles to 0
count = 0

# shuffle the deck
shuffledDeck = shuffle(cards)
# increment the number of shuffles by 1 because you just shuffled the deck
count = count + 1

# while the shuffledDeck does not equal the original order loop over and over again
while cards != shuffledDeck:
    
    # shuffle the deck
    shuffledDeck = shuffle(shuffledDeck)

    # increment the count
    count = count + 1

# print the number of shuffles it took to get back to the original deck order
print(count)