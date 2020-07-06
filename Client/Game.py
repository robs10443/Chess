import Board as brd
import Pieces
import game_config as gc

def movePiece(start_row,start_col,end_row,end_col):
    brd.board[end_row][end_col] = brd.board[start_row][start_col]
    brd.board[start_row][start_col] = None

pawn_with_enpassant = (-1,-1)

def moveOnBoard(start_row,start_col,end_row,end_col):
    global pawn_with_enpassant

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
    isInCheck()
    return True
    
def pawnPromotion(start_row,start_col,end_row,end_col,name_of_piece):
    global pawn_with_enpassant
    
    pawn_with_enpassant = (-1,-1)
    brd.board[start_row][start_col] = None
    if name_of_piece == "Queen":
        brd.board[end_row][end_col] = Pieces.Queen(gc.GAME_COLOR)
    
    if name_of_piece == "Rook":
        brd.board[end_row][end_col] = Pieces.Rook(gc.GAME_COLOR)
    
    if name_of_piece == "Bishop":
        brd.board[end_row][end_col] = Pieces.Bishop(gc.GAME_COLOR)
    
    if name_of_piece == "Knight":
        brd.board[end_row][end_col] = Pieces.Knight(gc.GAME_COLOR)

    isInCheck()
    
def doCastling(start_row,start_col,end_row,end_col):
    global pawn_with_enpassant
    
    pawn_with_enpassant = (-1,-1)
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
    isInCheck()

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
    
    if (flag_for_checkmate == True):
        print("You are checkmated Bad Luck!! :(")
    brd.board[row_of_king][col_of_king].setIncheck(True)

def checkmated():
    pass