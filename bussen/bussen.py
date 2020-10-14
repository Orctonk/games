from board import *
from deck import *
from player import *

deck = Deck()
board = Board(7,deck)
player = GoodAI()

# board.print()

tries = 50000
triesleft = tries
wins = 0

while(True):
    inp = player.getMove(board.getRefRank())

    res = board.guess(inp)

    # for i in range(board.size):
    #     print("\033[F\033[K", end="")
    
    # board.print()

    if not res[0]:
        triesleft -= 1
        if triesleft == 0:
            break
        player.getGameOverRestart()
        board.refill(deck)
        # for i in range(board.size + 1):
        #     print("\033[F\033[K", end="")
        # board.print()
    
    if res[1]:
        wins += 1
        triesleft -= 1
        if triesleft == 0:
            break
        player.onWin()
        board.refill(deck)
        # for i in range(board.size + 1):
        #     print("\033[F\033[K", end="")
        # board.print()

print('{0}/{1} ({2:.2%})'.format(wins, tries, float(wins)/tries))
