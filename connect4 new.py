# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 15:45:57 2022

@author: charlie, grace ,jayden, nicolas
"""

#N.A. commenting starts here
#Here is where specific modules are being imported. We see a familiar one from the lectures.
import numpy as np
import pygame
import sys
import math

#These are the colours of board, background, red chips, and yellow chips. They numbers in the brackets correspond to the 
#RGB colour model. In the brackets it goes (red,green,blue).
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

#Here we have the number of rows (6) and number of columns (7) being created
ROW_COUNT = 8#initize row variable
COLUMN_COUNT =9 #initize column variable
 
#Here, a function for creating the playing board is being defined. The board is made using the module numpy as np, and #the previous variables corresponding to the number of rows and columns.

def create_board():
    #this function is to in initize a board. at first the board will be empty
  
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board
 
#The function defined here is to drop the pieces into the board, at specific row and column locations.
  
def drop_piece(board, row, col, piece):
    board[row][col] = piece
#Next, this function is meant to check if a piece was placed in a valid location. There must be nothing in that #location, hence the '0'.
def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

# in the next few function definitions, r refers to row, and c refers to column
#This function is meant to place a piece in the next open row?
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r
#The defined function here is used to print the board when changes are made to it (updated with added pieces shown).
def print_board(board):
    print(np.flip(board, 0))

#This function is meant to check if there is 4 in a row horizontally. It checks if there are 4 pieces in a row from an #initial position c (that's why there are things like c+1, c+2, c+3). r must be constant for this to be the case because #it only counts horizontally. If there are 4 in a row horizontally, then True is returned and there is a winner.
def winning_move(board, piece):
  #Check horizontal locations for win
  i=0
  for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece and board[r][c+4]:
                i+=1
                if i==2:
                    return True
 
#This function acts like the previous one, except this time it check if there are 4 in a row vertically. There must be 4 pieces from an initial position r, and then r+1, r+2, r+3 all must follow. c is constant because only the rows are being counted, not the columns True is returned if there are 4 in a row vertically and there is a winner.
# Check vertical locations for win
              
  for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
          if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece and board[r+4][c]==piece:
                i+=1
                if i==2:
                    return True
 
#This function, like the previous two, checks if there are 4 pieces in a row. This time it is diagonally upward though (think like a positively sloped graph).
#To do this it counts one to the left or right from c, and then one up from row. If there are 4 in row with a positive slope, then True is returned and there is a winner.
#Check positively sloped diaganols
    
  for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece and board[r+4][c+4] == piece:
                i+=1
                if i==2:
                    return True
 
#This function is like the last one except it counts diagonally downward (with like a negative slope). The only difference is that it counts down from initial r position.
# Check negatively sloped diaganols
  for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece and board[r-4][c+4] == piece:
                i+=1
                if i==2:
                    return True
def winning_move2(board, piece):
  #Check horizontal locations for win
  i=0
  for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece and board[r][c+4]:
                i+=1
                if i==2:
                    return True
 
#This function acts like the previous one, except this time it check if there are 4 in a row vertically. There must be 4 pieces from an initial position r, and then r+1, r+2, r+3 all must follow. c is constant because only the rows are being counted, not the columns True is returned if there are 4 in a row vertically and there is a winner.
# Check vertical locations for win
              
  for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
          if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece and board[r+4][c]==piece:
                i+=1
                if i==2:
                    return True
 
#This function, like the previous two, checks if there are 4 pieces in a row. This time it is diagonally upward though (think like a positively sloped graph).
#To do this it counts one to the left or right from c, and then one up from row. If there are 4 in row with a positive slope, then True is returned and there is a winner.
#Check positively sloped diaganols
    
  for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece and board[r+4][c+4] == piece:
                i+=1
                if i==2:
                    return True
 
#This function is like the last one except it counts diagonally downward (with like a negative slope). The only difference is that it counts down from initial r position.
# Check negatively sloped diaganols
  for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece and board[r-4][c+4] == piece:
                i+=1
                if i==2:
                    return True
 
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
     
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):      
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2: 
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()
 
 
board = create_board()
print_board(board)
game_over = False
turn = 0
 
#initalize pygame
pygame.init()
 
#define our screen size
SQUARESIZE = 100
 
#define width and height of board
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
 
size = (width, height)
 
RADIUS = int(SQUARESIZE/2 - 5)
 
screen = pygame.display.set_mode(size)
#Calling function draw_board again
draw_board(board)
pygame.display.update()
 
myfont = pygame.font.SysFont("monospace", 75)
 
while not game_over:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
 
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else: 
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()
 
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
#print(event.pos)
# Ask for Player 1 Input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
 
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)
 
                    if winning_move(board, 1)==True:
                        label = myfont.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (40,10))
                        game_over = True
 
 
# # Ask for Player 2 Input
            else:               
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
 
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)
 
                    if winning_move2(board, 2)==True:
                        label = myfont.render("Player 2 wins!!", 1, YELLOW)
                        screen.blit(label, (40,10))
                        game_over = True
 
            print_board(board)
            draw_board(board)
 
            turn += 1
            turn = turn % 2
 
            if game_over:
                pygame.time.wait(3000)
