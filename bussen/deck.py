import random

suits = ['♠','♥','♦','♣']
ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

def getRank(card):
    if card[0] == 'A':
        return 1
    elif card[0] == 'J':
        return 11
    elif card[0] == 'Q':
        return 12
    elif card[0] == 'K':
        return 13
    else:
        return int(card[0])

class Deck():
    def __init__(self):
        super().__init__()
        self.deck = []
        for s in suits:
            for r in ranks:
                self.deck.append(r + s)
        random.shuffle(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def shuffle_in(self,cards):
        self.deck.extend(cards)
        self.shuffle()
    
    def draw(self):
        drawn = random.choice(self.deck)
        self.deck.remove(drawn)
        return drawn

    
    