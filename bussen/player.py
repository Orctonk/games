from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def getMove(self, refrank):
        pass

    @abstractmethod
    def giveReveal(self, row, cell, card):
        pass

    @abstractmethod
    def getGameOverRestart(self):
        pass

    @abstractmethod
    def onWin(self):
        pass

class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def getMove(self,refrank):
        while(True):
            inp = input("[l|r][l|h|s] ({}): " % refrank)
            print("\033[K", end="")
            if (len(inp) == 2) and (inp[0] in 'rl') and (inp[1] in 'lhs'):
                return inp
            print("Invalid input!\033[F\033[K",end = "")

    def giveReveal(self, cards):
        pass

    def getGameOverRestart(self):
        input("...")
        print("\033[F\033[K", end="")
        pass

    def onWin(self):
        input("You win!")
        print("\033[F\033[K", end="")

class RandomAI(Player):
    def __init__(self):
        super().__init__()
    
    def getMove(self,refrank):
        move = ''
        if random.randint(0,1) == 0:
            move += 'l'
        else:
            move += 'r'

        rankguess = random.randint(0,13)

        if rankguess < 7:
            move += 'l'
        elif rankguess > 7:
            move += 'h'
        else:
            move += 's'

        return move
    
    def giveReveal(self, cards):
        pass

    def getGameOverRestart(self):
        #input("...")
        pass

    def onWin(self):
        #input("ROBOWIN")
        pass

class SimpleAI(Player):
    def __init__(self):
        super().__init__()
    
    def getMove(self,refrank):
        move = ''
        if random.randint(0,1) == 0:
            move += 'l'
        else:
            move += 'r'

        rankguess = random.randint(0,13)

        if rankguess < refrank:
            move += 'l'
        elif rankguess > refrank:
            move += 'h'
        else:
            move += 's'

        return move
    
    def giveReveal(self, cards):
        pass

    def getGameOverRestart(self):
        #input("...")
        pass

    def onWin(self):
        #input("ROBOWIN")
        pass

class GoodAI(Player):
    def __init__(self):
        super().__init__()
    
    def getMove(self,refrank):
        move = ''
        if random.randint(0,1) == 0:
            move += 'l'
        else:
            move += 'r'

        if refrank >= 7:
            move += 'l'
        elif refrank < 7:
            move += 'h'

        return move
    
    def giveReveal(self, cards):
        pass

    def getGameOverRestart(self):
        #input("...")
        pass

    def onWin(self):
        #input("ROBOWIN")
        pass