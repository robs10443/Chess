import Board as brd
import Pieces as pc
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
    print(row_of_pawn_with_enpassant,col_of_pawn_with_enpassant)
    pawn_with_enpassant = (-1,-1)
    if row_of_pawn_with_enpassant != -1:
        brd.board[row_of_pawn_with_enpassant][col_of_pawn_with_enpassant].setEnpassant(False)
    
    notation = brd.getPiece(start_row,end_col)
    print (start_row,start_col)
    if(notation[1] == "P"):
        if(brd.board[start_row][start_col].getMoveTime() == 0):
            brd.board[start_row][start_col].setMoveTime(1)
            if ((start_row - end_row) == 2 or (start_row - end_row) == -2):
                brd.board[start_row][start_col].setEnpassant(True)
                pawn_with_enpassant = (end_row,end_col)
    
    
    movePiece(start_row,start_col,end_row,end_col)
    return True
    
