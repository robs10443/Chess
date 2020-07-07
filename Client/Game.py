import Board as brd
import Pieces
import game_config as gc

def movePiece(start_row,start_col,end_row,end_col):
    brd.board[end_row][end_col] = brd.board[start_row][start_col]
    brd.board[start_row][start_col] = None

pawn_with_enpassant = (-1,-1)

def moveOnBoard(start_row,start_col,end_row,end_col):
    global pawn_with_enpassant

    attacking_list = brd.isAttacked(gc.GAME_COLOR)
    row_of_king,col_of_king = brd.findPieceOfSameColor(gc.GAME_COLOR,"King")
    if (row_of_king,col_of_king) not in attacking_list:
        brd.board[row_of_king][col_of_king].setIncheck(False)

    row_of_pawn_with_enpassant,col_of_pawn_with_enpassant = pawn_with_enpassant
    pawn_with_enpassant = (-1,-1)
    if row_of_pawn_with_enpassant != -1:
        brd.board[row_of_pawn_with_enpassant][col_of_pawn_with_enpassant].setEnpassant(False)
    
    notation = brd.getPiece(start_row,start_col)
    if(notation[1] == "P"):
        if(brd.board[start_row][start_col].getMoveTime() == 0):
            brd.board[start_row][start_col].setMoveTime(1)
            if ((start_row - end_row) == 2 or (start_row - end_row) == -2):
                brd.board[start_row][start_col].setEnpassant(True)
                pawn_with_enpassant = (end_row,end_col)
        
        if (end_col == (start_col - 1)):
            if(brd.isNone(end_row,end_col) == True):
                brd.board[start_row][end_col] = None
        if (end_col == (start_col + 1)):
            if(brd.isNone(end_row,end_col) == True):
                brd.board[start_row][end_col] = None

    if(notation[1] == 'R' and notation[0].lower() == gc.GAME_COLOR[0].lower()):
        brd.board[start_row][start_col].setIsMoved(True)

    if(notation[1] == 'K' and notation[0].lower() == gc.GAME_COLOR[0].lower()):
        brd.board[start_row][start_col].setLongCastle(False)
        brd.board[start_row][start_col].setShortCastle(False)

    movePiece(start_row,start_col,end_row,end_col)
    attacking_list = brd.isAttacked(gc.GAME_COLOR)
    row_of_king,col_of_king = brd.findPieceOfSameColor(gc.GAME_COLOR,"King")
    if (row_of_king,col_of_king) not in attacking_list:
        brd.board[row_of_king][col_of_king].setIncheck(False)
    
    return True
    
def pawnPromotion(flag,start_row,start_col,end_row,end_col,name_of_piece):
    attacking_list = brd.isAttacked(gc.GAME_COLOR)
    row_of_king,col_of_king = brd.findPieceOfSameColor(gc.GAME_COLOR,"King")
    if (row_of_king,col_of_king) not in attacking_list:
        brd.board[row_of_king][col_of_king].setIncheck(False)
    
    global pawn_with_enpassant
    color = ""
    if(flag == 0):
        if(gc.GAME_COLOR == "Black"):
            color = "White"
        else:
            color = "Black"
    else:
        color = gc.GAME_COLOR
    pawn_with_enpassant = (-1,-1)
    brd.board[start_row][start_col] = None
    if name_of_piece.lower() == "Queen".lower():
        brd.board[end_row][end_col] = Pieces.Queen(color)
    
    if name_of_piece.lower() == "Rook".lower():
        brd.board[end_row][end_col] = Pieces.Rook(color)
    
    if name_of_piece.lower() == "Bishop".lower():
        brd.board[end_row][end_col] = Pieces.Bishop(color)
    
    if name_of_piece.lower() == "Knight".lower():
        brd.board[end_row][end_col] = Pieces.Knight(color)

    attacking_list = brd.isAttacked(gc.GAME_COLOR)
    row_of_king,col_of_king = brd.findPieceOfSameColor(gc.GAME_COLOR,"King")
    if (row_of_king,col_of_king) not in attacking_list:
        brd.board[row_of_king][col_of_king].setIncheck(False)
    

    
def doCastling(start_row,start_col,end_row,end_col):
    global pawn_with_enpassant
    
    attacking_list = brd.isAttacked(gc.GAME_COLOR)
    row_of_king,col_of_king = brd.findPieceOfSameColor(gc.GAME_COLOR,"King")
    if (row_of_king,col_of_king) not in attacking_list:
        brd.board[row_of_king][col_of_king].setIncheck(False)

    pawn_with_enpassant = (-1,-1)
    if(gc.GAME_COLOR == "White"):
        if ((end_col - start_col) == 2):
            brd.board[start_row][start_col + 1] = brd.board[start_row][start_col + 3]
            brd.board[start_row][start_col + 1].setIsMoved(True)
            brd.board[start_row][start_col + 3] = None
            brd.board[start_row][end_col] = brd.board[start_row][start_col]
            brd.board[start_row][start_col] = None
        else:
            brd.board[start_row][start_col - 1] = brd.board[start_row][start_col - 4]
            brd.board[start_row][start_col - 1].setIsMoved(True)
            brd.board[start_row][start_col - 4] = None
            brd.board[start_row][end_col] = brd.board[start_row][start_col]
            brd.board[start_row][start_col] = None
    else:
        if ((end_col - start_col) == -2):
            brd.board[start_row][start_col - 1] = brd.board[start_row][start_col - 3]
            brd.board[start_row][start_col - 1].setIsMoved(True)
            brd.board[start_row][start_col - 3] = None
            brd.board[start_row][end_col] = brd.board[start_row][start_col]
            brd.board[start_row][start_col] = None
        else:
            brd.board[start_row][start_col + 1] = brd.board[start_row][start_col + 4]
            brd.board[start_row][start_col + 1].setIsMoved(True)
            brd.board[start_row][start_col + 4] = None
            brd.board[start_row][end_col] = brd.board[start_row][start_col]
            brd.board[start_row][start_col] = None
    
    attacking_list = brd.isAttacked(gc.GAME_COLOR)
    row_of_king,col_of_king = brd.findPieceOfSameColor(gc.GAME_COLOR,"King")
    if (row_of_king,col_of_king) not in attacking_list:
        brd.board[row_of_king][col_of_king].setIncheck(False)
    

def isInCheck():
    attacking_list = brd.isAttacked(gc.GAME_COLOR)
    row_of_king,col_of_king = brd.findPieceOfSameColor(gc.GAME_COLOR,"King")
    if (row_of_king,col_of_king) not in attacking_list:
        brd.board[row_of_king][col_of_king].setIncheck(False)
        return False
    flag_for_checkmate = True
    for row in range(gc.BOX_COUNT_PER_SIDE):
        for col in range(gc.BOX_COUNT_PER_SIDE):
            if (brd.getPieceColor(row,col) == gc.GAME_COLOR):
                if(len(brd.getMoves(row,col)) >= 1):
                    flag_for_checkmate = False
                    break
        if(flag_for_checkmate == False):
            break
    brd.board[row_of_king][col_of_king].setIncheck(True)
    if (flag_for_checkmate == True):
        return True
    return False

def checkmated():
    pass

def wonByCheckmate():
    exit()