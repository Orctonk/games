import math

from deck import getRank

ops = { 
    'l' : lambda l,r: l < r,
    'h' : lambda l,r: l > r,
    's' : lambda l,r: l == r
}

class Board:
    def __init__(self, size, deck):
        super().__init__()
        self.size = size
        self.width = math.ceil(self.size/2)
        self.maxindex = self.width - 1
        self.cards = []
        self.rev = []
        self.ppos = (0,0)
        self.currank = 7
        self.revcards = []
        for i in range(-self.maxindex, self.maxindex + 1):
            self.cards.append([])
            self.rev.append([])
            index = i + self.maxindex
            for j in range(self.width-abs(i)):
                self.cards[index].append(deck.draw())
                self.rev[index].append(False)

    def refill(self,deck):
        self.ppos = (0,0)
        self.currank = 7
        deck.shuffle_in(self.revcards)
        self.revcards = []
        for (r,row) in enumerate(self.rev):
            for (c,cell) in enumerate(row):
                if cell:
                    self.rev[r][c] = False
                    self.cards[r][c] = deck.draw()

    def print(self):
        for i in range(-self.maxindex, self.maxindex + 1):
            index = i + self.maxindex
            print('  ' * abs(i), end='')
            for j in range(self.width-abs(i)):
                if self.rev[index][j]:
                    print(self.cards[index][j], end='')
                    if len(self.cards[index][j]) == 2:
                        print(" ", end="")
                    print(" ",end="")
                else:
                    print('[]  ', end='')
            print("")

    def getRefRank(self):
        return self.currank

    def guess(self,guess):
        chosencard = 0
        if self.ppos[1] != 0 and self.ppos[1] != self.size-1:
            if self.ppos[1] < self.width:
                if guess[0] == 'l':
                    chosencard = self.ppos[0]
                elif guess[0] == 'r':
                    chosencard = self.ppos[0] + 1
            else:
                if guess[0] == 'l':
                    chosencard = self.ppos[0] - 1
                elif guess[0] == 'r':
                    chosencard = self.ppos[0]
        if chosencard < 0:
            chosencard = 0
        elif chosencard > (self.maxindex - abs(self.maxindex - self.ppos[1])):
            chosencard = self.maxindex - abs(self.maxindex - self.ppos[1])

        self.rev[(self.size-1) - self.ppos[1]][chosencard] = True
        card = self.cards[(self.size-1) - self.ppos[1]][chosencard]
        self.revcards.append(card)
        rank = getRank(card)
        if ops[guess[1]](rank,self.currank):
            self.ppos = (chosencard, self.ppos[1] + 1)
            self.currank = rank
        else:
            return (False,False,card)
        return (True,self.ppos[1] == self.size,card)