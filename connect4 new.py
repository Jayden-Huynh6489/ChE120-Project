# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 15:45:57 2022

@author: Charlie, Grace, Jayden, Nicolas
"""


import numpy as np
import pygame
import sys
import math


BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

ROW_COUNT = 8#initize row variable
COLUMN_COUNT =9 #initize column variable


def create_board():
  
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board
 
  
def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r
def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
  #Check horizontal locations for win
  i=0
  for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece and board[r][c+4]:
                i+=1
                if i==2:
                    return True
 
              
  for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
          if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece and board[r+4][c]==piece:
                i+=1
                if i==2:
                    return True
 
    
  for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece and board[r+4][c+4] == piece:
                i+=1
                if i==2:
                    return True
 
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
 
#This function acts like the previous one, except this time it check if there are 4 in a row vertically. 
#There must be 4 pieces from an initial position r, and then r+1, r+2, r+3 all must follow. c is constant because only 
#the rows are being counted, not the columns True is returned if there are 4 in a row vertically and there is a winner. N.A.
# Check vertical locations for win
              
  for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
          if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece and board[r+4][c]==piece:
                i+=1
                if i==2:
                    return True
 
#This function, like the previous two, checks if there are 4 pieces in a row. This time it is diagonally upward though (think like a positively sloped graph).
#To do this it counts one to the left or right from c, and then one up from row. 
#If there are 4 in row with a positive slope, then True is returned and there is a winner. N.A.
#Check positively sloped diaganols
    
  for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece and board[r+4][c+4] == piece:
                i+=1
                if i==2:
                    return True
 

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
