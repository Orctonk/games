from obj import Circle,Board
from constants import *
import ai

import pygame as pg
import random as rn
import copy

pg.init()
screen = pg.display.set_mode(W_SIZE)

g_lbimg = pg.transform.scale(pg.image.load("lb.png").convert_alpha(),(H_WIDTH,H_HEIGHT))
g_diceimg = pg.transform.scale(pg.image.load("dice.png").convert_alpha(),(H_WIDTH,H_HEIGHT))
g_a_canvas = pg.Surface(W_SIZE,pg.SRCALPHA,32)

def drawGui(guess,sources,activeRow):
    g_a_canvas.fill((0,0,0,0))
    if not init:
        for p in activeRow:
            pg.draw.circle(g_a_canvas,BRD_HOLE,p,DOT_RADIUS)
        g_a_canvas.blit(g_diceimg,(H_X,H_Y))
    else:
        g_a_canvas.blit(g_lbimg,(H_X,H_Y))
        (_,p) = ai.getRow(brd.getHistory(),brd.getResults())
        f = pg.font.Font(pg.font.get_default_font(),12)
        ptext = f.render("{}".format(p),True,(0,0,0))
        g_a_canvas.blit(ptext,(G_X_SPAN+8,A_Y * 2 - 5 - 12))
    for c in sources + guess:
        if c != None:
            c.draw(g_a_canvas)
    if dragC != None:
        shadow = copy.copy(dragC)
        shadow.pos = (shadow.pos[0] + 5,shadow.pos[1] + 5)
        shadow.col = (0,0,0,125)
        shadow.draw(g_a_canvas)
        dragC.draw(g_a_canvas)

    return g_a_canvas

dragC = None
brd = Board()
init = False

guess = [None,None,None,None]
activeRow = []
for x in range(G_X_INIT,G_X_SPAN,G_X_SPACING):
    activeRow.append((x,A_Y))

sources = []
for (i,x) in enumerate(range(C_INIT,W_WIDTH,C_SPACING)):
    sources.append(Circle((x,C_Y),DOT_RADIUS,COLORS[i]))

win = False
run = True
while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
        elif e.type == pg.MOUSEBUTTONDOWN:
            mpos = pg.mouse.get_pos()
            if mpos[0] > G_X_SPAN and mpos[1] < A_Y * 2:
                if init:
                    history = brd.getHistory()
                    res = brd.getResults()
                    aig = ai.getRow(history,res)
                    brd.postGuess(aig[0])
                    if brd.gameover:
                        brd.showAns = True
                        if res[0] == 4:
                            win = True
                else:
                    ans = []
                    for i in range(4):
                        ans.append(rn.randint(1,6))
                    brd.setAns(ans)
                    init = True
                guess = [None,None,None,None]
                activeRow = brd.getActiveRow()
                continue
            for c in sources+guess:
                if c == None:
                    continue
                if c.isInside(mpos):
                    if c in sources:
                        dragC = copy.copy(c)
                    else:
                        dragC = c
                        guess[guess.index(c)] = None
                    break
        elif e.type == pg.MOUSEBUTTONUP:
            if dragC != None:
                for (i,p) in enumerate(activeRow):
                    if dragC.isInside(p):
                        dragC.move(p)
                        guess[i] = dragC
                        break
                dragC = None
            gc = True
            for c in guess:
                if c == None:
                    gc = False
            if gc:
                if not init:
                    brd.setAns(list(map(lambda item: COLORS.index(item.col) + 1,guess)))
                    guess = [None,None,None,None]
                    activeRow = brd.getActiveRow()
                    init = True
                else:
                    res = brd.postGuess(list(map(lambda item: COLORS.index(item.col) + 1,guess)))
                    if brd.gameover:
                        brd.showAns = True
                        if res[0] == 4:
                            win = True
                    guess = [None,None,None,None]
                    activeRow = brd.getActiveRow()
        elif e.type == pg.MOUSEMOTION:
            if dragC != None:
                dragC.move(e.pos)

    brd.draw(screen)
    
    ac = drawGui(guess,sources,activeRow)
    screen.blit(ac,(0,0))
    pg.display.update()

pg.quit()