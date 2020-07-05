import Board as brd
import Pieces as pc
import GUI as gui
import game_config as gc
import threading

def initGame(color):
    gc.GAME_COLOR = color
    brd.init(color)
    gui.displayScreen()

def movePiece(start_row,start_col,end_row,end_col):
    brd.board[end_row][end_col] = brd.board[start_row][start_col]
    brd.board[start_row][start_col] = None

def moveOnBoard(start_row,start_col,end_row,end_col):
    if ((end_row,end_col) in brd.board[start_row][start_col].moves):
        movePiece(start_row,start_col,end_row,end_col)

initGame("White")