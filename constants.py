COLORS      =   [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (255,175,0), (255,0,255)]
W_SIZE      =   (W_WIDTH,W_HEIGHT) = (400,800)

DOT_RADIUS  =   15
RES_RADIUS  =   7

G_X_SPAN    =   int(W_WIDTH * 3 / 4)
G_X_SPACING =   int(G_X_SPAN / 4)
G_X_INIT    =   int(G_X_SPACING / 2)
G_Y_SPAN    =   int(W_HEIGHT * 6 / 8)
G_Y_SPACING =   int(G_Y_SPAN / 6)
G_Y_INIT    =   int(W_HEIGHT * 7 / 8 - G_X_SPACING / 2)

A_Y         =   int(W_HEIGHT / 16)

C_SPACING   =   int(W_WIDTH / 6)
C_INIT      =   int(C_SPACING / 2)
C_Y         =   int(W_HEIGHT * 7.5 / 8)

R_SPACING   =   int(G_Y_SPACING/3)  
R_X_INIT    =   int(W_WIDTH * 3.5 / 4 - R_SPACING/2)

BRD_FG      =   (150,75,0)
BRD_HL      =   (170,85,0)
BRD_HOLE    =   (60,30,0)
BRD_EXT     =   (180,90,0)
BRD_SHD     =   (110,55,0)