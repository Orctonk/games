############# GAME WINDOW OPTIONS #############
# The size of the window
W_SIZE      =   (W_WIDTH,W_HEIGHT) = (400,800)

############# BOARD OPTIONS #############
# Radii for items
DOT_RADIUS  =   15
RES_RADIUS  =   7

# Initial position, span and spacing for guesses
G_X_SPAN    =   int(W_WIDTH * 3 / 4)
G_X_SPACING =   int(G_X_SPAN / 4)
G_X_INIT    =   int(G_X_SPACING / 2)
G_Y_SPAN    =   int(W_HEIGHT * 6 / 8)
G_Y_SPACING =   int(G_Y_SPAN / 6)
G_Y_INIT    =   int(W_HEIGHT * 7 / 8 - G_X_SPACING / 2)

# The Y position of the answer
A_Y         =   int(W_HEIGHT / 16)

# The initial x position, spacing and y position of the choices
C_SPACING   =   int(W_WIDTH / 6)
C_INIT      =   int(C_SPACING / 2)
C_Y         =   int(W_HEIGHT * 7.5 / 8)

# The spacing and initial x position for the result pins
R_SPACING   =   int(G_Y_SPACING/3)  
R_X_INIT    =   int(W_WIDTH * 3.5 / 4 - R_SPACING/2)

############# OPTION-PANE OPTIONS #############

# Position and size of the hint/randomize button
H_X         =   int(W_WIDTH * 3.1 / 4)
H_Y         =   int(W_HEIGHT * 0.1 / 8)
H_WIDTH     =   int(W_WIDTH * 0.8 / 4)
H_HEIGHT    =   int(H_Y * 8)

############## COLORS ##############
# The colors use
COLORS      =   [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (255,175,0), (255,0,255)]
BRD_FG      =   (150,75,0)      # Board
BRD_HL      =   (170,85,0)      # Highlight
BRD_HOLE    =   (80,40,0)       # Hole
BRD_EXT     =   (180,90,0)      # Extrusions
BRD_SHD     =   (110,55,0)      # Shadow