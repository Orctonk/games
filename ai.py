import random as rn

def getRight(guess, ans):
    black = 0
    white = 0
    taken = []
    for i in range(4):
        if int(guess[i]) == ans[i]:
            black += 1
            taken.append(i)
        else:
            for j in range(4):
                if int(guess[j]) != ans[j] and int(guess[i]) == ans[j] and not j in taken:
                    white += 1
                    taken.append(j)

    return (black,white)

def filterByGuess(guess,res,possible):
    return list(filter(lambda l1: getRight(guess,l1) == res,possible))

def getRow(history,res):
    possible = []

    for a in range(1,7):
        for b in range(1,7):
            for c in range(1,7):
                for d in range(1,7):
                    possible.append([a,b,c,d])

    for i in range(len(history)):
        possible = filterByGuess(history[i],res[i],possible)

    if len(possible) == 1:
        return (possible[0],1)
    else:
        return (possible[rn.randrange(0,len(possible) - 1)],len(possible))