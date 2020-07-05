import Board
import game_config as gc

class King:
    def __init__(self,color):
        self.long_castle = False
        self.short_castle = False
        self.notation = color[0].upper() + "K"
        self.is_move = False

    def getNotation(self):
        return self.notation

    def getColor(self):
        if(self.notation[0] == 'B'):
            return "Black"
        else:
            return "White"

    def setLongCastle(self,flag):
        self.long_castle = flag
    
    def setShortCastle(self,flag):
        self.short_castle = flag

    def isLongCastle(self):
        return self.long_castle
    
    def isShortCastle(self):
        return self.short_castle

    def moves(self,row,col):
        attacking_list = Board.isAttacked(self.getColor())
        diffent_king_x, diffent_king_y = Board.findPiece(gc.GAME_COLOR,"King")

        for t1 in [1,0,-1]:
            for t2 in [1,0,-1]:
                if((diffent_king_x + t1,diffent_king_y + t2) not in attacking_list):
                    attacking_list.append((diffent_king_x + t1,diffent_king_y + t2))

        list_of_moves = []
        tx = 1
        ty = 0
        # print (row + tx,col + ty)
        if Board.isInboard(row + tx,col + ty) == True and (row + tx,col + ty) not in attacking_list  and Board.isSameColor(row,col,row + tx,col + ty) == False :
            list_of_moves.append((row + tx,col + ty))
        
        tx = 1
        ty = -1
        # print (row + tx,col + ty)
        if Board.isInboard(row + tx,col + ty) == True and (row + tx,col + ty) not in attacking_list and Board.isSameColor(row,col,row + tx,col + ty) == False :
            list_of_moves.append((row + tx,col + ty))
        
        tx = 1
        ty = 1
        # print (row + tx,col + ty)
        if Board.isInboard(row + tx,col + ty) == True and (row + tx,col + ty) not in attacking_list and Board.isSameColor(row,col,row + tx,col + ty) == False :
            list_of_moves.append((row + tx,col + ty))
        
        tx = -1
        ty = 0
        # print (row + tx,col + ty)
        if Board.isInboard(row + tx,col + ty) == True and (row + tx,col + ty) not in attacking_list  and Board.isSameColor(row,col,row + tx,col + ty) == False :
            list_of_moves.append((row + tx,col + ty))
        
        tx = -1
        ty = 1
        # print (row + tx,col + ty)
        if Board.isInboard(row + tx,col + ty) == True and (row + tx,col + ty) not in attacking_list  and Board.isSameColor(row,col,row + tx,col + ty) == False :
            list_of_moves.append((row + tx,col + ty))
        
        tx = -1
        ty = -1
        # print (row + tx,col + ty)
        if Board.isInboard(row + tx,col + ty) == True and (row + tx,col + ty) not in attacking_list  and Board.isSameColor(row,col,row + tx,col + ty) == False :
            list_of_moves.append((row + tx,col + ty))
        
        tx = 0
        ty = 1
        # print (row + tx,col + ty)
        if Board.isInboard(row + tx,col + ty) == True and (row + tx,col + ty) not in attacking_list  and Board.isSameColor(row,col,row + tx,col + ty) == False :
            list_of_moves.append((row + tx,col + ty))
        
        tx = 0
        ty = -1
        # print (row + tx,col + ty)
        if Board.isInboard(row + tx,col + ty) == True and (row + tx,col + ty) not in attacking_list  and Board.isSameColor(row,col,row + tx,col + ty) == False :
            list_of_moves.append((row + tx,col + ty))
        
        if self.isShortCastle():
            list_of_moves.append((row, col + 2))

        if self.isLongCastle():
            list_of_moves.append((row,col - 2))

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
        self.first_move = False

    def getNotation(self):
        return self.notation

    def getColor(self):
        if(self.notation[0] == 'B'):
            return "Black"
        else:
            return "White"

    def isFirstMove(self):
        return self.first_move

    def setFirstMove(self,flag):
        self.first_move = flag

    def attackingMoves(self,row,col):
        list_of_moves = []
        if Board.isInboard(row + 1,col - 1) == True:
            list_of_moves.append((row + 1,col - 1))
        if Board.isInboard(row + 1,col + 1) == True:
            list_of_moves.append((row + 1,col + 1))
        
        return list_of_moves
        

    def moves(self,row,col):
        list_of_moves = []
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
        return list_of_moves
