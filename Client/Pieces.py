import Board
import game_config as gc

class King:
    def __init__(self,color):
        self.long_castle = True
        self.short_castle = True
        self.notation = color[0].upper() + "K"
        self.is_move = False
        self.in_check = False

    def getNotation(self):
        return self.notation

    def getColor(self):
        if(self.notation[0] == 'B'):
            return "Black"
        else:
            return "White"

    def setIncheck(self,flag):
        self.in_check = flag
    
    def getIncheck(self):
        return self.in_check

    def setLongCastle(self,flag):
        self.long_castle = flag
    
    def setShortCastle(self,flag):
        self.short_castle = flag

    def isLongCastle(self):
        return self.long_castle
    
    def isShortCastle(self):
        return self.short_castle

    def checkForAttackingPiece(self,row,col):
        flag = True
        if(Board.getPiece(row,col)[0] != gc.GAME_COLOR[0]):
            temp = Board.board[row][col]
            Board.board[row][col] = None
            if (row,col) in Board.isAttacked(self.getColor()):
                flag = False
            Board.board[row][col] = temp
        return flag

    def filteredMoves(self,row,col):
        if(self.getColor() != gc.GAME_COLOR):
            return []
        list_of_moves = self.moves(row,col)
        return Board.filterMovesForKing(list_of_moves,row,col)

    def moves(self,row,col):
        attacking_list = Board.isAttacked(self.getColor())
        diffent_king_x, diffent_king_y = Board.findPieceOfOppositeColor(gc.GAME_COLOR,"King")

        for t1 in [1,0,-1]:
            for t2 in [1,0,-1]:
                if Board.isInboard(diffent_king_x + t1,diffent_king_y + t2) == True and ((diffent_king_x + t1,diffent_king_y + t2) not in attacking_list):
                    attacking_list.append((diffent_king_x + t1,diffent_king_y + t2))

        list_of_moves = []
        tx = 1
        ty = 0
        if Board.isInboard(row + tx,col + ty) == True and (row + tx,col + ty) not in attacking_list  and Board.isSameColor(row,col,row + tx,col + ty) == False :
            if(self.checkForAttackingPiece(row + tx,col + ty) == True):
                list_of_moves.append((row + tx,col + ty))
        
        tx = 1
        ty = -1
        if Board.isInboard(row + tx,col + ty) == True and (row + tx,col + ty) not in attacking_list and Board.isSameColor(row,col,row + tx,col + ty) == False :
            if(self.checkForAttackingPiece(row + tx,col + ty) == True):
                list_of_moves.append((row + tx,col + ty))
        
        tx = 1
        ty = 1
        if Board.isInboard(row + tx,col + ty) == True and (row + tx,col + ty) not in attacking_list and Board.isSameColor(row,col,row + tx,col + ty) == False :
            if(self.checkForAttackingPiece(row + tx,col + ty) == True):
                list_of_moves.append((row + tx,col + ty))
        
        tx = -1
        ty = 0
        if Board.isInboard(row + tx,col + ty) == True and (row + tx,col + ty) not in attacking_list  and Board.isSameColor(row,col,row + tx,col + ty) == False :
            if(self.checkForAttackingPiece(row + tx,col + ty) == True):
                list_of_moves.append((row + tx,col + ty))
        
        tx = -1
        ty = 1
        if Board.isInboard(row + tx,col + ty) == True and (row + tx,col + ty) not in attacking_list  and Board.isSameColor(row,col,row + tx,col + ty) == False :
            if(self.checkForAttackingPiece(row + tx,col + ty) == True):
                list_of_moves.append((row + tx,col + ty))
        
        tx = -1
        ty = -1
        if Board.isInboard(row + tx,col + ty) == True and (row + tx,col + ty) not in attacking_list  and Board.isSameColor(row,col,row + tx,col + ty) == False :
            if(self.checkForAttackingPiece(row + tx,col + ty) == True):
                list_of_moves.append((row + tx,col + ty))
        
        tx = 0
        ty = 1
        if Board.isInboard(row + tx,col + ty) == True and (row + tx,col + ty) not in attacking_list  and Board.isSameColor(row,col,row + tx,col + ty) == False :
            if(self.checkForAttackingPiece(row + tx,col + ty) == True):
                list_of_moves.append((row + tx,col + ty))
        
        tx = 0
        ty = -1
        if Board.isInboard(row + tx,col + ty) == True and (row + tx,col + ty) not in attacking_list  and Board.isSameColor(row,col,row + tx,col + ty) == False :
            if(self.checkForAttackingPiece(row + tx,col + ty) == True):
                list_of_moves.append((row + tx,col + ty))
        
        if (gc.GAME_COLOR == "White"):
            if self.isShortCastle() and (self.getIncheck() == False):
                if Board.isInboard(row,col + 1) == True and Board.isInboard(row,col + 2) == True and Board.isInboard(row,col + 3) == True:
                    if Board.isNone(row,col + 1) == True and Board.isNone(row,col + 2) == True and Board.isNone(row,col + 3) == False and Board.board[row][col + 3].IsMoved() == False:
                        if (row,col + 1) not in attacking_list and (row,col + 2) not in attacking_list:
                            list_of_moves.append((row, col + 2))

            if self.isLongCastle() and self.getIncheck() == False:
                if Board.isInboard(row,col - 1) == True and Board.isInboard(row,col - 2) == True and Board.isInboard(row,col - 3) == True and Board.isInboard(row,col - 4) == True:
                    if Board.isNone(row,col - 1) == True and Board.isNone(row,col - 2) == True and Board.isNone(row,col - 3) == True and Board.isNone(row,col - 4) == False and Board.board[row][col - 4].IsMoved() == False:
                        if (row,col - 1) not in attacking_list and (row,col - 2) not in attacking_list:
                            list_of_moves.append((row, col - 2))
        else:
            if self.isShortCastle() and self.getIncheck() == False:
                if Board.isInboard(row,col - 1) == True and Board.isInboard(row,col - 2) == True and Board.isInboard(row,col - 3) == True:
                    if Board.isNone(row,col - 1) == True and Board.isNone(row,col - 2) == True and Board.isNone(row,col - 3) == False and Board.board[row][col - 3].IsMoved() == False:
                        if (row,col - 1) not in attacking_list and (row,col - 2) not in attacking_list:
                            list_of_moves.append((row, col - 2))

            if self.isLongCastle() and self.getIncheck() == False:
                if Board.isInboard(row,col + 1) == True and Board.isInboard(row,col + 2) == True and Board.isInboard(row,col + 3) == True and Board.isInboard(row,col + 4) == True:
                    if Board.isNone(row,col + 1) == True and Board.isNone(row,col + 2) == True and Board.isNone(row,col + 3) == True and Board.isNone(row,col + 4) == False and Board.board[row][col + 4].IsMoved() == False:
                        if (row,col + 1) not in attacking_list and (row,col + 2) not in attacking_list:
                            list_of_moves.append((row, col + 2))
		
        return list_of_moves

class Queen:
    def __init__(self,color):
        self.notation = color[0].upper() + "Q"

    def getColor(self):
        if(self.notation[0] == 'B'):
            return "Black"
        else:
            return "White"

    def getNotation(self):
        return self.notation

    def filteredMoves(self,row,col):
        if(self.getColor() != gc.GAME_COLOR):
            return []
        list_of_moves = self.moves(row,col)
        return Board.filterMovesInCheck(list_of_moves,row,col)

    def moves(self,row,col):
        list_of_moves = []
        tx = 1
        ty = 1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(row + tx*i,col + ty*i) == False:
                break
            if Board.isNone(row + tx*i,col + ty*i):
                list_of_moves.append((row + tx*i,col + ty*i))
            elif Board.isSameColor(row,col,row + tx*i,col + ty*i) == False:
                list_of_moves.append((row + tx*i,col + ty*i))
                break
            else:
                break
        
        tx = 1
        ty = -1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(row + tx*i,col + ty*i) == False:
                break
            if Board.isNone(row + tx*i,col + ty*i):
                list_of_moves.append((row + tx*i,col + ty*i))
            elif Board.isSameColor(row,col,row + tx*i,col + ty*i) == False:
                list_of_moves.append((row + tx*i,col + ty*i))
                break
            else:
                break
        

        tx = -1
        ty = 1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(row + tx*i,col + ty*i) == False:
                break
            if Board.isNone(row + tx*i,col + ty*i):
                list_of_moves.append((row + tx*i,col + ty*i))
            elif Board.isSameColor(row,col,row + tx*i,col + ty*i) == False:
                list_of_moves.append((row + tx*i,col + ty*i))
                break
            else:
                break
        
        tx = -1
        ty = -1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(row + tx*i,col + ty*i) == False:
                break
            if Board.isNone(row + tx*i,col + ty*i):
                list_of_moves.append((row + tx*i,col + ty*i))
            elif Board.isSameColor(row,col,row + tx*i,col + ty*i) == False:
                list_of_moves.append((row + tx*i,col + ty*i))
                break
            else:
                break
        
        tx = 1
        ty = 1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(row + tx*i,col) == False:
                break
            if Board.isNone(row + tx*i,col) == True:
                list_of_moves.append((row + tx*i,col))
            elif Board.isSameColor(row,col,row + tx*i,col) == False:
                list_of_moves.append((row + tx*i,col))
                break
            else:
                break
        
        tx = 1
        ty = -1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(row,col + ty*i) == False:
                break
            if Board.isNone(row,col + ty*i):
                list_of_moves.append((row,col + ty*i))
            elif Board.isSameColor(row,col,row,col + ty*i) == False:
                list_of_moves.append((row,col + ty*i))
                break
            else:
                break
        

        tx = -1
        ty = 1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(row + tx*i,col) == False:
                break
            if Board.isNone(row + tx*i,col):
                list_of_moves.append((row + tx*i,col))
            elif Board.isSameColor(row,col,row + tx*i,col) == False:
                list_of_moves.append((row + tx*i,col))
                break
            else:
                break
        
        tx = -1
        ty = 1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(row,col + ty*i) == False:
                break
            if Board.isNone(row,col + ty*i):
                list_of_moves.append((row,col + ty*i))
            elif Board.isSameColor(row,col,row,col + ty*i) == False:
                list_of_moves.append((row,col + ty*i))
                break
            else:
                break
        return list_of_moves
        
        

class Rook:
    def __init__(self,color):
        self.notation = color[0].upper() + "R"
        self.is_moved = False

    def getNotation(self):
        return self.notation

    def getColor(self):
        if(self.notation[0] == 'B'):
            return "Black"
        else:
            return "White"

    def setIsMoved(self,flag):
        self.is_moved = flag

    def IsMoved(self):
        return self.is_moved

    def filteredMoves(self,row,col):
        if(self.getColor() != gc.GAME_COLOR):
            return []
        list_of_moves = self.moves(row,col)
        return Board.filterMovesInCheck(list_of_moves,row,col)

    def moves(self,row,col):
        list_of_moves = []
        tx = 1
        ty = 1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(row + tx*i,col) == False:
                break
            if Board.isNone(row + tx*i,col) == True:
                list_of_moves.append((row + tx*i,col))
            elif Board.isSameColor(row,col,row + tx*i,col) == False:
                list_of_moves.append((row + tx*i,col))
                break
            else:
                break
        
        tx = 1
        ty = -1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(row,col + ty*i) == False:
                break
            if Board.isNone(row,col + ty*i):
                list_of_moves.append((row,col + ty*i))
            elif Board.isSameColor(row,col,row,col + ty*i) == False:
                list_of_moves.append((row,col + ty*i))
                break
            else:
                break
        

        tx = -1
        ty = 1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(row + tx*i,col) == False:
                break
            if Board.isNone(row + tx*i,col):
                list_of_moves.append((row + tx*i,col))
            elif Board.isSameColor(row,col,row + tx*i,col) == False:
                list_of_moves.append((row + tx*i,col))
                break
            else:
                break
        
        tx = -1
        ty = 1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(row,col + ty*i) == False:
                break
            if Board.isNone(row,col + ty*i):
                list_of_moves.append((row,col + ty*i))
            elif Board.isSameColor(row,col,row,col + ty*i) == False:
                list_of_moves.append((row,col + ty*i))
                break
            else:
                break
        
        return list_of_moves

class Bishop:
    def __init__(self,color):
        self.notation = color[0].upper() + "B"
        
    def getNotation(self):
        return self.notation

    def getColor(self):
        if(self.notation[0] == 'B'):
            return "Black"
        else:
            return "White"

    def filteredMoves(self,row,col):
        if(self.getColor() != gc.GAME_COLOR):
            return []
        list_of_moves = self.moves(row,col)
        return Board.filterMovesInCheck(list_of_moves,row,col)

    def moves(self,row,col):
        list_of_moves = []
        tx = 1
        ty = 1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(row + tx*i,col + ty*i) == False:
                break
            if Board.isNone(row + tx*i,col + ty*i):
                list_of_moves.append((row + tx*i,col + ty*i))
            elif Board.isSameColor(row,col,row + tx*i,col + ty*i) == False:
                list_of_moves.append((row + tx*i,col + ty*i))
                break
            else:
                break
        
        tx = 1
        ty = -1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(row + tx*i,col + ty*i) == False:
                break
            if Board.isNone(row + tx*i,col + ty*i):
                list_of_moves.append((row + tx*i,col + ty*i))
            elif Board.isSameColor(row,col,row + tx*i,col + ty*i) == False:
                list_of_moves.append((row + tx*i,col + ty*i))
                break
            else:
                break
        

        tx = -1
        ty = 1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(row + tx*i,col + ty*i) == False:
                break
            if Board.isNone(row + tx*i,col + ty*i):
                list_of_moves.append((row + tx*i,col + ty*i))
            elif Board.isSameColor(row,col,row + tx*i,col + ty*i) == False:
                list_of_moves.append((row + tx*i,col + ty*i))
                break
            else:
                break
        
        tx = -1
        ty = -1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(row + tx*i,col + ty*i) == False:
                break
            if Board.isNone(row + tx*i,col + ty*i):
                list_of_moves.append((row + tx*i,col + ty*i))
            elif Board.isSameColor(row,col,row + tx*i,col + ty*i) == False:
                list_of_moves.append((row + tx*i,col + ty*i))
                break
            else:
                break
        
        return list_of_moves



class Knight:
    def __init__(self,color):
        self.notation = color[0].upper() + "N"
        
    def getNotation(self):
        return self.notation

    def getColor(self):
        if(self.notation[0] == 'B'):
            return "Black"
        else:
            return "White"

    def filteredMoves(self,row,col):
        if(self.getColor() != gc.GAME_COLOR):
            return []
        list_of_moves = self.moves(row,col)
        return Board.filterMovesInCheck(list_of_moves,row,col)

    def moves(self,row,col):
        list_of_moves = []

        if Board.isInboard(row + 1,col + 2) == True and Board.isSameColor(row,col,row + 1,col + 2) == False:
            list_of_moves.append((row + 1,col + 2))
        
        if Board.isInboard(row + 1,col - 2) == True and Board.isSameColor(row,col,row + 1,col - 2) == False:
            list_of_moves.append((row + 1,col - 2))
        
        if Board.isInboard(row - 1,col + 2) == True and Board.isSameColor(row,col,row - 1,col + 2) == False:
            list_of_moves.append((row - 1,col + 2))
        
        if Board.isInboard(row - 1,col - 2) == True and Board.isSameColor(row,col,row - 1,col - 2) == False:
            list_of_moves.append((row - 1,col - 2))
        
        if Board.isInboard(row + 2,col + 1) == True and Board.isSameColor(row,col,row + 2,col + 1) == False:
            list_of_moves.append((row + 2,col + 1))
        
        if Board.isInboard(row + 2,col - 1) == True and Board.isSameColor(row,col,row + 2,col - 1) == False:
            list_of_moves.append((row + 2,col - 1))
        
        if Board.isInboard(row - 2,col + 1) == True and Board.isSameColor(row,col,row - 2,col + 1) == False:
            list_of_moves.append((row - 2,col + 1))
        
        if Board.isInboard(row - 2,col - 1) == True and Board.isSameColor(row,col,row - 2,col - 1) == False:
            list_of_moves.append((row - 2,col - 1))
        
        return list_of_moves

class Pawn:
    def __init__(self,color):
        self.notation = color[0].upper() + "P"
        self.first_move = 0
        self.enPassant = False

    def getNotation(self):
        return self.notation

    def getColor(self):
        if(self.notation[0] == 'B'):
            return "Black"
        else:
            return "White"

    def setEnpassant(self,flag):
        self.enPassant = flag

    def getEnpassant(self):
        return self.enPassant

    def getMoveTime(self):
        return self.first_move

    def setMoveTime(self,flag):
        self.first_move = flag

    def attackingMoves(self,row,col):
        list_of_moves = []
        if Board.isInboard(row + 1,col - 1) == True:
            list_of_moves.append((row + 1,col - 1))
        if Board.isInboard(row + 1,col + 1) == True:
            list_of_moves.append((row + 1,col + 1))
        
        return list_of_moves
        
    def filteredMoves(self,row,col):
        if(self.getColor() != gc.GAME_COLOR):
            return []
        list_of_moves = self.moves(row,col)
        return Board.filterMovesInCheck(list_of_moves,row,col)

    def moves(self,row,col):
        list_of_moves = []
        
        color_of_the_current_pawn = self.getColor()

        if (color_of_the_current_pawn[0] == gc.GAME_COLOR[0]):
            if self.getMoveTime() == 0:
                if ((row - 1) >= 0):
                    if Board.isPiece(row - 1,col) == False:
                        list_of_moves.append((row - 1,col))
                        if((row - 2) >= 0):
                            if Board.isPiece(row - 2,col) == False:
                                list_of_moves.append((row - 2,col))
                    
                    if (col + 1) < gc.BOX_COUNT_PER_SIDE:
                        if Board.isPiece(row - 1,col + 1) == True and Board.isSameColor(row,col,row - 1,col + 1) == False:
                            list_of_moves.append((row - 1,col + 1))
                    
                    if((col - 1) >= 0) and Board.isSameColor(row,col,row - 1,col - 1) == False:
                        if Board.isPiece(row - 1, col - 1) == True:
                            list_of_moves.append((row - 1,col - 1))
            else:
                if ((row - 1) >= 0):
                    if Board.isPiece(row - 1,col) == False:
                        list_of_moves.append((row - 1,col))
                    
                    if (col + 1) < gc.BOX_COUNT_PER_SIDE:
                        if Board.isPiece(row - 1,col + 1) == True and Board.isSameColor(row,col,row - 1,col + 1) == False:
                            list_of_moves.append((row - 1,col + 1))
                    
                    if((col - 1) >= 0) and Board.isSameColor(row,col,row - 1,col - 1) == False:
                        if Board.isPiece(row - 1, col - 1) == True:
                            list_of_moves.append((row - 1,col - 1))
            
            if Board.isInboard(row,col - 1) == True and Board.isNone(row,col - 1) == False:
                notation = Board.board[row][col - 1].getNotation()
                if notation[1] == 'P' and notation[0] != gc.GAME_COLOR[0]:
                    if Board.board[row][col - 1].getEnpassant() == True:
                        list_of_moves.append((row - 1,col - 1))
            
            if Board.isInboard(row,col + 1) == True and Board.isNone(row,col + 1) == False :
                notation = Board.board[row][col + 1].getNotation()
                if notation[1] == 'P' and notation[0] != gc.GAME_COLOR[0]:
                    if Board.board[row][col + 1].getEnpassant() == True:
                        list_of_moves.append((row - 1,col + 1))
        else:
            if self.getMoveTime() == 0:
                if ((row + 1) < gc.TOTAL_NUMBER_OF_BOXES):
                    if Board.isPiece(row + 1,col) == False:
                        list_of_moves.append((row + 1,col))
                        if((row + 2) >= 0):
                            if Board.isPiece(row + 2,col) == False:
                                list_of_moves.append((row + 2,col))
                    
                    if (col + 1) < gc.BOX_COUNT_PER_SIDE:
                        if Board.isPiece(row + 1,col + 1) == True and Board.isSameColor(row,col,row + 1,col + 1) == False:
                            list_of_moves.append((row + 1,col + 1))
                    
                    if((col - 1) >= 0) and Board.isSameColor(row,col,row + 1,col - 1) == False:
                        if Board.isPiece(row + 1, col - 1) == True:
                            list_of_moves.append((row + 1,col - 1))
            else:
                if ((row + 1) < gc.TOTAL_NUMBER_OF_BOXES):
                    if Board.isPiece(row + 1,col) == False:
                        list_of_moves.append((row + 1,col))
                    
                    if (col + 1) < gc.BOX_COUNT_PER_SIDE:
                        if Board.isPiece(row + 1,col + 1) == True and Board.isSameColor(row,col,row + 1,col + 1) == False:
                            list_of_moves.append((row + 1,col + 1))
                    
                    if((col - 1) >= 0) and Board.isSameColor(row,col,row + 1,col - 1) == False:
                        if Board.isPiece(row + 1, col - 1) == True:
                            list_of_moves.append((row + 1,col - 1))
            
            if Board.isInboard(row,col - 1) == True and Board.isNone(row,col - 1) == False:
                notation = Board.board[row][col - 1].getNotation()
                if notation[1] == 'P' and notation[0] == gc.GAME_COLOR[0]:
                    if Board.board[row][col - 1].getEnpassant() == True:
                        list_of_moves.append((row + 1,col - 1))
            
            if Board.isInboard(row,col + 1) == True and Board.isNone(row,col + 1) == False :
                notation = Board.board[row][col + 1].getNotation()
                if notation[1] == 'P' and notation[0] == gc.GAME_COLOR[0]:
                    if Board.board[row][col + 1].getEnpassant() == True:
                        list_of_moves.append((row + 1,col + 1))
        
        return list_of_moves
