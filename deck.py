import random
suits = ("Spades", "Diamonds", "Hearts", "Clubs")
rank = (1,2,3,4,5,6,7,8,9,10,11,12,13)

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def show(self):
        print self.rank, "of", self.suit

        if self.rank == 1:
            self.rank == "Ace"
        elif self.rank == 11:
            self.rank == "Jack"
        elif self.rank == 12:
            self.rank == "Queen"
        elif self.rank == 13:
            self.rank == "King"

class Deck(object):
    def __init__(self):
        self.size = 52
        self.content = []
    def newDeck(self):
        self.size = 52
        for rank in range(1, 14):
            self.content.append(Card(rank , "Clubs"))
        for rank in range(1, 14):
            self.content.append(Card(rank , "Diamonds"))
        for rank in range(1, 14):
            self.content.append(Card(rank , "Hearts"))
        for rank in range(1, 14):
            self.content.append(Card(rank , "Spades"))

        random.shuffle(self.content)
    def deal(self):
        return self.content.pop()

class User(object):
    def __init__(self, drawpile):
        self.hand = []
        self.drawpile = drawpile
    def showhand(self):
        for i in self.hand:
            i.show()
        return self
    def draw(self):
        self.hand.append(self.drawpile.deal())
        return self
    def fold(self):
        del hand[:]
    def play(self, choice):
        print "You played:"
        self.hand[choice].show()
        del self.hand[choice]

deck1 = Deck()
deck1.newDeck()
user1 = User(deck1)
user1.draw().draw().draw().showhand()
        

    
    




        