
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
        
    else:
        board[0][0] = Pieces.Rook("White")
        board[0][1] = Pieces.Knight("White")
        board[0][2] = Pieces.Bishop("White")
        board[0][3] = Pieces.King("White")
        board[0][4] = Pieces.Queen("White")
        board[0][5] = Pieces.Bishop("White")
        board[0][6] = Pieces.Knight("White")
        board[0][7] = Pieces.Rook("White")
        
        for x in range(8):
            board[1][x] = Pieces.Pawn("White")
        
        board[7][0] = Pieces.Rook("Black")
        board[7][1] = Pieces.Knight("Black")
        board[7][2] = Pieces.Bishop("Black")
        board[7][3] = Pieces.King("Black")
        board[7][4] = Pieces.Queen("Black")
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
    if(getPieceColor(x,y) != gc.GAME_COLOR):
        return []
    else:
        return board[x][y].filteredMoves(x,y)

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
                notation = board[row][col].getNotation()
                lst = []
                if(notation[1] == 'P'):
                    lst = board[row][col].attackingMoves(row,col)
                elif (notation[1] != 'K'):
                    lst = board[row][col].moves(row,col)
                for (x,y) in lst:
                    if (x,y) not in attacking_list:
                        attacking_list.append((x,y))
    return attacking_list

def findPieceOfOppositeColor(color,name_of_piece):
    for row in range(gc.BOX_COUNT_PER_SIDE):
        for col in range(gc.BOX_COUNT_PER_SIDE):
            if(board[row][col] != None):
                notation = board[row][col].getNotation()
                if(notation[0].lower() != color[0].lower() and notation[1].lower() == name_of_piece[0].lower()):
                    return row,col
    return -1,-1

def findPieceOfSameColor(color,name_of_piece):
    for row in range(gc.BOX_COUNT_PER_SIDE):
        for col in range(gc.BOX_COUNT_PER_SIDE):
            if(board[row][col] != None):
                notation = board[row][col].getNotation()
                if(notation[0].lower() == color[0].lower() and notation[1].lower() == name_of_piece[0].lower()):
                    return row,col
    return -1,-1

def filterMovesInCheck(list_of_moves,row,col):
    row_of_king,col_of_king = findPieceOfSameColor(gc.GAME_COLOR,"King")
    temp_original = board[row][col]
    board[row][col] = None
    new_list = []
    for moves_row,moves_col in list_of_moves:
        temp_destination = board[moves_row][moves_col]
        board[moves_row][moves_col] = temp_original
        attacking_list = isAttacked(gc.GAME_COLOR)
        if (row_of_king,col_of_king) not in attacking_list:
            new_list.append((moves_row,moves_col))
        board[moves_row][moves_col] = temp_destination
    board[row][col] = temp_original
    return new_list

def filterMovesForKing(list_of_moves,row,col):
    temp_original = board[row][col]
    board[row][col] = None
    new_list = []
    for moves_row,moves_col in list_of_moves:
        temp_destination = board[moves_row][moves_col]
        board[moves_row][moves_col] = temp_original
        attacking_list = isAttacked(gc.GAME_COLOR)
        if (moves_row,moves_col) not in attacking_list:
            new_list.append((moves_row,moves_col))
        board[moves_row][moves_col] = temp_destination
    board[row][col] = temp_original
    return new_list