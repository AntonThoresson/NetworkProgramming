import random as r

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit

    def __str__(self):
        suitName = ["", "Spades", "Hearts", "Diamonds", "Clubs"]
        valueName = ["", "Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        return valueName[self.value] + " of " + suitName[self.suit] 

class CardDeck():
    def __init__(self):
        self.cardDeck = list()
        self.reset()

    def shuffle(self):
        r.seed(42)
        r.shuffle(self.cardDeck)
        r.seed()

    def getCard(self):
        card = self.cardDeck.pop()
        return card

    def size(self):
        return len(self.cardDeck)
    
    def reset(self):
        self.cardDeck.clear()
        for suit in range(1,5):
            for value in range(1,14):
                card = Card(suit, value)
                self.cardDeck.append(card)


deck = CardDeck()
deck.shuffle()
while deck.size() > 0:
    card = deck.getCard()
    print("Card {} has value {} and suit value {}".format(card, card.getValue(), card.getSuit()))


