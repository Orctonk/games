import pygame as pg
import random as rn

TILE_SIZE = (TILE_WIDTH,TILE_HEIGHT) = (32,32)
TILE_COUNT = (TILE_X_COUNT,TILE_Y_COUNT) = (20,20)
BORDER_SIZE = 3
TILE_STIRDE = (TILE_X_STRIDE,TILE_Y_STRIDE) = (TILE_WIDTH+BORDER_SIZE,TILE_HEIGHT+BORDER_SIZE)
MINE_COUNT = 25
WINDOW_SIZE = (WINDOW_WIDTH,WINDOW_HEIGHT) = (TILE_X_COUNT*TILE_X_STRIDE,TILE_Y_COUNT*TILE_Y_STRIDE)

pg.init()
screen = pg.display.set_mode(WINDOW_SIZE)

class Tile:
    mine_img = pg.transform.scale(pg.image.load("mine.png").convert_alpha(),TILE_SIZE)
    flag_img = pg.transform.scale(pg.image.load("flag.png").convert_alpha(),TILE_SIZE)
    def __init__(self, pos: tuple, mine: bool):
        self.pos = pos
        self.count = 0
        self.marked = False
        self.isMine = mine
        self.revealed = False

    def draw(self, canvas, gameover = False):
        drawRect = pg.Rect((self.pos[0]*TILE_X_STRIDE,self.pos[1]*TILE_Y_STRIDE),TILE_SIZE)
        if self.isMine:
            if gameover:
                pg.draw.rect(canvas,(255,0,0),drawRect)
                canvas.blit(Tile.mine_img,drawRect.topleft)
            else:
                pg.draw.rect(canvas,(100,100,100),drawRect)
                if self.marked:
                    canvas.blit(Tile.flag_img,drawRect.topleft)
        else:
            if self.revealed:
                pg.draw.rect(canvas,(200,200,200),drawRect)
                if self.count > 0:
                    text = pg.font.SysFont("Consolas",TILE_HEIGHT).render("{}".format(self.count),False,(0,0,0))
                    canvas.blit(text,(drawRect.left + 5,drawRect.top + 5))
            else:
                pg.draw.rect(canvas,(100,100,100),drawRect)
                if self.marked:
                    canvas.blit(Tile.flag_img,drawRect.topleft)

def count_mines(board: list, pos: tuple) -> int:
    count = 0
    for x in range(-1,2):
        for y in range(-1,2):
            if x==0 and y==0:
                continue

            xc = pos[0] + x
            yc = pos[1] + y

            if xc < 0 or yc < 0 or xc >=TILE_X_COUNT or yc>=TILE_Y_COUNT:
                continue

            if board[yc][xc].isMine:
                count += 1
    return count

def revealAdjacent(board: list, pos: tuple):
    poslist = [pos]

    while len(poslist) != 0:
        pos = poslist.pop()
        board[pos[1]][pos[0]].revealed = True

        if board[pos[1]][pos[0]].count == 0:
            for x in range(-1,2):
                for y in range(-1,2):
                    xc = pos[0] + x
                    yc = pos[1] + y

                    if xc < 0 or yc < 0 or xc >=TILE_X_COUNT or yc>=TILE_Y_COUNT:
                        continue
                    if not board[yc][xc].revealed:
                        poslist.append((xc,yc))

def generateBoard():
    board = []
    mines = []
    while len(mines) < MINE_COUNT:
        candidate = rn.randint(0,TILE_X_COUNT*TILE_Y_COUNT - 1)
        if not candidate in mines:
            mines.append(candidate)

    for y in range(TILE_Y_COUNT):
        board.append([])
        for x in range(TILE_X_COUNT):
            ismine = (y * TILE_X_COUNT + x) in mines
            board[y].append(Tile((x,y),ismine))

    for y in range(TILE_Y_COUNT):
        for x in range(TILE_X_COUNT):
            board[y][x].count = count_mines(board,(x,y))
    return board

board = generateBoard()
run = True
gameover = False
while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
        elif e.type == pg.MOUSEBUTTONDOWN:
            if not gameover:
                mpos = pg.mouse.get_pos()
                xpos = int(mpos[0] / TILE_X_STRIDE)
                ypos = int(mpos[1] / TILE_Y_STRIDE)
                if e.button == 1:
                    board[ypos][xpos].revealed = True
                    if board[ypos][xpos].isMine:
                        gameover = True
                    else:
                        revealAdjacent(board,(xpos,ypos))
                elif e.button == 3:
                    board[ypos][xpos].marked = not board[ypos][xpos].marked

    screen.fill((0,0,0))
    for row in board:
        for t in row:
            t.draw(screen,gameover)
    pg.display.flip()

pg.quit()