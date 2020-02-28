import pygame as pg
from typing import List

from constants import *

class Circle:
    def __init__(self, pos: tuple, rad: int, color: tuple) -> None:
        self.pos = pos
        self.rad = rad
        self.col = color
    
    def move(self, pos: tuple) -> None:
        self.pos = pos

    def isInside(self, point: tuple) -> bool:
        distSqr = (self.pos[0]-point[0])**2 + (self.pos[1]-point[1])**2
        return distSqr <= self.rad ** 2

    def draw(self,surf) -> None:
        pg.draw.circle(surf,self.col,self.pos,self.rad)

class Board:
    def __init__(self):
        self.ans = None
        self.showAns = False
        self.rect = pg.Rect(0,0,W_WIDTH,W_HEIGHT)
        self.history = []
        self.res = []
        self.gameover = False

    def setAns(self, ans: List[int]) -> None:
        self.ans = ans

    def getHistory(self) -> List[int]:
        return self.history

    def getResults(self) -> List[tuple]:
        return self.res

    def getGameOver(self) -> bool:
        return self.gameover

    def postGuess(self, guess: List[int]) -> tuple:
        if self.gameover:
            return (4,4)
        self.history.append(guess)
        black = 0
        white = 0
        taken = []
        for i in range(4):
            if int(guess[i]) == self.ans[i]:
                black += 1
                taken.append(i)
            else:
                for j in range(4):
                    if int(guess[j]) != self.ans[j] and int(guess[i]) == self.ans[j] and not j in taken:
                        white += 1
                        taken.append(j)
                        break
        self.res.append((black,white))
        if black == 4 or len(self.history) == 6:
            self.gameover = True
        return (black,white)

    def getActiveRow(self) -> List[tuple]:
        rowNum = len(self.history)
        retList = []
        for x in range(G_X_INIT,G_X_SPAN,G_X_SPACING):
            retList.append((x,G_Y_INIT - rowNum*G_Y_SPACING))
        return retList

    def _drawHistory_(self,surf) ->  None:    
        for i in range(6):
            if i >= len(self.history):
                for x in range(G_X_INIT,G_X_SPAN,G_X_SPACING):
                    pg.draw.circle(surf,BRD_HOLE,(x,G_Y_INIT - i*G_Y_SPACING),DOT_RADIUS)
                for j in range(4):
                    pos = (R_X_INIT + (j%2)*R_SPACING, G_Y_INIT - i*G_Y_SPACING + (int(-R_SPACING/2) + int(j/2) * R_SPACING))
                    pg.draw.circle(surf,BRD_HOLE,pos,RES_RADIUS)
            else:
                for (h,x) in enumerate(range(G_X_INIT,G_X_SPAN,G_X_SPACING)):
                    c = self.history[i][h] - 1
                    pg.draw.circle(surf,COLORS[c],(x,G_Y_INIT - i*G_Y_SPACING),DOT_RADIUS)
                for j in range(4):
                    pos = (R_X_INIT + (j%2)*R_SPACING, G_Y_INIT - i*G_Y_SPACING + (int(-R_SPACING/2) + int(j/2) * R_SPACING))
                    if j < self.res[i][0]:
                        pg.draw.circle(surf,(0,0,0),pos,RES_RADIUS)
                    elif j < self.res[i][0] + self.res[i][1]:
                        pg.draw.circle(surf,(255,255,255),pos,RES_RADIUS)
                    else:
                        pg.draw.circle(surf,BRD_HOLE,pos,RES_RADIUS)


    def draw(self, surf) -> None:
        pg.draw.rect(surf,BRD_FG,self.rect)
        # pg.draw.rect(surf,BRD_HL,(0, G_Y_INIT - (len(self.history) + 1) * G_Y_SPACING,G_X_SPAN,G_Y_SPACING))
        pg.draw.line(surf,BRD_EXT,(0,2*A_Y),(G_X_SPAN,2*A_Y),3)
        pg.draw.line(surf,BRD_SHD,(0,2*A_Y + 3),(G_X_SPAN,2*A_Y + 3),3)
        pg.draw.line(surf,BRD_EXT,(G_X_SPAN,0),(G_X_SPAN,G_Y_SPAN + G_Y_SPACING),3)
        pg.draw.line(surf,BRD_SHD,(G_X_SPAN + 3,0),(G_X_SPAN+3,G_Y_SPAN + G_Y_SPACING),3)
        pg.draw.line(surf,BRD_EXT,(G_X_SPAN+2,2*A_Y),(W_WIDTH,2*A_Y),3)
        pg.draw.line(surf,BRD_SHD,(G_X_SPAN+2,2*A_Y + 3),(W_WIDTH,2*A_Y + 3),3)
        pg.draw.line(surf,BRD_EXT,(0,G_Y_SPAN + G_Y_SPACING),(W_WIDTH,G_Y_SPAN + G_Y_SPACING),3)
        pg.draw.line(surf,BRD_SHD,(0,G_Y_SPAN + G_Y_SPACING + 3),(W_WIDTH,G_Y_SPAN + G_Y_SPACING + 3),3)

        if self.showAns:
            for (i,x) in enumerate(range(G_X_INIT,G_X_SPAN,G_X_SPACING)):
                pg.draw.circle(surf,COLORS[self.ans[i] - 1],(x,A_Y),DOT_RADIUS)

        self._drawHistory_(surf)

        
         