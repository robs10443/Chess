
board = [[None for _ in range(8)] for _ in range(8)]

import Pieces
import game_config as gc

def init(color):
    
    #intialization of board based on the color
    if color.lower() == "white":
        board[0][0] = Pieces.Rook("Black")
        board[0][1] = Pieces.Knight("Black")
        board[0][2] = Pieces.Bishop("Black")
        board[0][3] = Pieces.Queen("Black")
        board[0][4] = Pieces.King("Black")
        board[0][5] = Pieces.Bishop("Black")
        board[0][6] = Pieces.Knight("Black")
        board[0][7] = Pieces.Rook("Black")
        
        for x in range(8):
            board[1][x] = Pieces.Pawn("Black")
        
        board[7][0] = Pieces.Rook("White")
        board[7][1] = Pieces.Knight("White")
        board[7][2] = Pieces.Bishop("White")
        board[7][3] = Pieces.Queen("White")
        board[7][4] = Pieces.King("White")
        board[7][5] = Pieces.Bishop("White")
        board[7][6] = Pieces.Knight("White")
        board[7][7] = Pieces.Rook("White")
        
        for x in range(8):
            board[6][x] = Pieces.Pawn("White")
        
        board[5][3] = Pieces.Queen("Black")
        board[5][1] = Pieces.Queen("White")
        
    else:
        board[0][0] = Pieces.Rook("White")
        board[0][1] = Pieces.Knight("White")
        board[0][2] = Pieces.Bishop("White")
        board[0][3] = Pieces.Queen("White")
        board[0][4] = Pieces.King("White")
        board[0][5] = Pieces.Bishop("White")
        board[0][6] = Pieces.Knight("White")
        board[0][7] = Pieces.Rook("White")
        
        for x in range(8):
            board[1][x] = Pieces.Pawn("White")
        
        board[7][0] = Pieces.Rook("Black")
        board[7][1] = Pieces.Knight("Black")
        board[7][2] = Pieces.Bishop("Black")
        board[7][3] = Pieces.Queen("Black")
        board[7][4] = Pieces.King("Black")
        board[7][5] = Pieces.Bishop("Black")
        board[7][6] = Pieces.Knight("Black")
        board[7][7] = Pieces.Rook("Black")
        
        for x in range(8):
            board[6][x] = Pieces.Pawn("Black")
        
        
        

def getPiece(x,y):
    if board[x][y] == None:
        return "."
    return board[x][y].getNotation()

def getPieceColor(x,y):
    if board[x][y] == None:
        return ""
    return board[x][y].getColor()

def isPiece(x,y):
    if board[x][y] == None:
        return False
    else:
        return True

def getMoves(x,y):
    if board[x][y] == None:
        return []
    return board[x][y].moves(x,y)

def isInboard(x,y):
    if x >= 0 and x < gc.BOX_COUNT_PER_SIDE and y >= 0 and y < gc.BOX_COUNT_PER_SIDE:
        return True
    return False

def isSameColor(first_x,first_y,second_x,second_y):
    if board[second_x][second_y] == None:
        return False
    if board[first_x][first_y].getColor() == board[second_x][second_y].getColor():
        return True
    return False

def isNone(x,y):
    if board[x][y] == None:
        return True
    return False

def isAttacked(color_of_piece):
    attacking_list = []
    for row in range(gc.BOX_COUNT_PER_SIDE):
        for col in range(gc.BOX_COUNT_PER_SIDE):
            if isNone(row,col) == False and color_of_piece != getPieceColor(row,col):
                lst = board[row][col].moves(row,col)
                for (x,y) in lst:
                    if (x,y) not in attacking_list:
                        attacking_list.append((x,y))
        
    return attacking_list