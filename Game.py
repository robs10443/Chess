import Board as brd
import Pieces
import game_config as gc

def movePiece(start_row,start_col,end_row,end_col):
    brd.board[end_row][end_col] = brd.board[start_row][start_col]
    brd.board[start_row][start_col] = None

pawn_with_enpassant = (-1,-1)

def moveOnBoard(start_row,start_col,end_row,end_col):
    if ((end_row,end_col) not in brd.board[start_row][start_col].moves(start_row,start_col)):
        return False
    
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
    

    movePiece(start_row,start_col,end_row,end_col)
    return True
    
def pawnPromotion(start_row,start_col,end_row,end_col,name_of_piece):
    brd.board[start_row][start_col] = None
    if name_of_piece == "Queen":
        brd.board[end_row][end_col] = Pieces.Queen(gc.GAME_COLOR)
    
    if name_of_piece == "Rook":
        brd.board[end_row][end_col] = Pieces.Rook(gc.GAME_COLOR)
    
    if name_of_piece == "Bishop":
        brd.board[end_row][end_col] = Pieces.Bishop(gc.GAME_COLOR)
    
    if name_of_piece == "Knight":
        brd.board[end_row][end_col] = Pieces.Knight(gc.GAME_COLOR)
    