from obj import Circle,Board
from constants import *
import ai

import pygame as pg
import copy


pg.init()
screen = pg.display.set_mode(W_SIZE)
a_canvas = pg.Surface(W_SIZE,pg.SRCALPHA,32)

lbimg = pg.transform.scale(pg.image.load("lb.png").convert_alpha(),(H_WIDTH,H_HEIGHT))

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
                history = brd.getHistory()
                res = brd.getResults()
                aig = ai.getRow(history,res)
                brd.postGuess(aig[0])
                if brd.gameover:
                    brd.showAns = True
                    if res[0] == 4:
                        win = True
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

    a_canvas.fill((0,0,0,0))
    brd.draw(screen)
    a_canvas.blit(lbimg,(H_X,H_Y))

    if not init:
        for p in activeRow:
            pg.draw.circle(screen,BRD_HOLE,p,DOT_RADIUS)
    for c in sources:
        c.draw(screen)
    for c in guess: 
        if c != None:
            c.draw(screen)
    if dragC != None:
        shadow = copy.copy(dragC)
        shadow.pos = (shadow.pos[0] + 5,shadow.pos[1] + 5)
        shadow.col = (0,0,0,125)
        shadow.draw(a_canvas)
        dragC.draw(a_canvas)

    if init:
        (_,p) = ai.getRow(brd.getHistory(),brd.getResults())
        f = pg.font.Font(pg.font.get_default_font(),12)
        ptext = f.render("{}".format(p),True,(0,0,0))
        screen.blit(ptext,(G_X_SPAN+8,A_Y * 2 - 5 - 12))
    
    screen.blit(a_canvas,(0,0))
    pg.display.update()

pg.quit()