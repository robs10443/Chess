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

    def isLongCastle(self,flag):
        return self.long_castle
    
    def isShortCastle(self,flag):
        return self.short_castle

    def moves(self,x,y):
        attacking_list = Board.isAttacked(self.getColor())
        list_of_moves = []
        tx = 1
        ty = 0
        # if Board.isInboard(x + tx,y + ty) == True and (x + tx,y + ty) not in attacking_list and Board.isSameColor(x,y,x + tx,y + ty) == False :
        #     list_of_moves.append((x + tx,y + ty))
        
        # tx = 1
        # ty = -1
        # if Board.isInboard(x + tx,y + ty) == True and (x + tx,y + ty) not in attacking_list and Board.isSameColor(x,y,x + tx,y + ty) == False :
        #     list_of_moves.append((x + tx,y + ty))
        
        # tx = 1
        # ty = 1
        # if Board.isInboard(x + tx,y + ty) == True and (x + tx,y + ty) not in attacking_list and Board.isSameColor(x,y,x + tx,y + ty) == False :
        #     list_of_moves.append((x + tx,y + ty))
        
        # tx = -1
        # ty = 0
        # if Board.isInboard(x + tx,y + ty) == True and (x + tx,y + ty) not in attacking_list and Board.isSameColor(x,y,x + tx,y + ty) == False :
        #     list_of_moves.append((x + tx,y + ty))
        
        # tx = -1
        # ty = 1
        # if Board.isInboard(x + tx,y + ty) == True and (x + tx,y + ty) not in attacking_list and Board.isSameColor(x,y,x + tx,y + ty) == False :
        #     list_of_moves.append((x + tx,y + ty))
        
        # tx = -1
        # ty = -1
        # if Board.isInboard(x + tx,y + ty) == True and (x + tx,y + ty) not in attacking_list and Board.isSameColor(x,y,x + tx,y + ty) == False :
        #     list_of_moves.append((x + tx,y + ty))
        
        # tx = 0
        # ty = 1
        # if Board.isInboard(x + tx,y + ty) == True and (x + tx,y + ty) not in attacking_list and Board.isSameColor(x,y,x + tx,y + ty) == False :
        #     list_of_moves.append((x + tx,y + ty))
        
        # tx = 0
        # ty = -1
        # if Board.isInboard(x + tx,y + ty) == True and (x + tx,y + ty) not in attacking_list and Board.isSameColor(x,y,x + tx,y + ty) == False :
        #     list_of_moves.append((x + tx,y + ty))
        
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

    def moves(self,x,y):
        list_of_moves = []
        tx = 1
        ty = 1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(x + tx*i,y + ty*i) == False:
                break
            if Board.isNone(x + tx*i,y + ty*i):
                list_of_moves.append((x + tx*i,y + ty*i))
            elif Board.isSameColor(x,y,x + tx*i,y + ty*i) == False:
                list_of_moves.append((x + tx*i,y + ty*i))
                break
            else:
                break
        
        tx = 1
        ty = -1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(x + tx*i,y + ty*i) == False:
                break
            if Board.isNone(x + tx*i,y + ty*i):
                list_of_moves.append((x + tx*i,y + ty*i))
            elif Board.isSameColor(x,y,x + tx*i,y + ty*i) == False:
                list_of_moves.append((x + tx*i,y + ty*i))
                break
            else:
                break
        

        tx = -1
        ty = 1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(x + tx*i,y + ty*i) == False:
                break
            if Board.isNone(x + tx*i,y + ty*i):
                list_of_moves.append((x + tx*i,y + ty*i))
            elif Board.isSameColor(x,y,x + tx*i,y + ty*i) == False:
                list_of_moves.append((x + tx*i,y + ty*i))
                break
            else:
                break
        
        tx = -1
        ty = -1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(x + tx*i,y + ty*i) == False:
                break
            if Board.isNone(x + tx*i,y + ty*i):
                list_of_moves.append((x + tx*i,y + ty*i))
            elif Board.isSameColor(x,y,x + tx*i,y + ty*i) == False:
                list_of_moves.append((x + tx*i,y + ty*i))
                break
            else:
                break
        
        tx = 1
        ty = 1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(x + tx*i,y) == False:
                break
            if Board.isNone(x + tx*i,y) == True:
                list_of_moves.append((x + tx*i,y))
            elif Board.isSameColor(x,y,x + tx*i,y) == False:
                list_of_moves.append((x + tx*i,y))
                break
            else:
                break
        
        tx = 1
        ty = -1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(x,y + ty*i) == False:
                break
            if Board.isNone(x,y + ty*i):
                list_of_moves.append((x,y + ty*i))
            elif Board.isSameColor(x,y,x,y + ty*i) == False:
                list_of_moves.append((x,y + ty*i))
                break
            else:
                break
        

        tx = -1
        ty = 1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(x + tx*i,y) == False:
                break
            if Board.isNone(x + tx*i,y):
                list_of_moves.append((x + tx*i,y))
            elif Board.isSameColor(x,y,x + tx*i,y) == False:
                list_of_moves.append((x + tx*i,y))
                break
            else:
                break
        
        tx = -1
        ty = 1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(x,y + ty*i) == False:
                break
            if Board.isNone(x,y + ty*i):
                list_of_moves.append((x,y + ty*i))
            elif Board.isSameColor(x,y,x,y + ty*i) == False:
                list_of_moves.append((x,y + ty*i))
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

    def moves(self,x,y):
        list_of_moves = []
        tx = 1
        ty = 1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(x + tx*i,y) == False:
                break
            if Board.isNone(x + tx*i,y) == True:
                list_of_moves.append((x + tx*i,y))
            elif Board.isSameColor(x,y,x + tx*i,y) == False:
                list_of_moves.append((x + tx*i,y))
                break
            else:
                break
        
        tx = 1
        ty = -1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(x,y + ty*i) == False:
                break
            if Board.isNone(x,y + ty*i):
                list_of_moves.append((x,y + ty*i))
            elif Board.isSameColor(x,y,x,y + ty*i) == False:
                list_of_moves.append((x,y + ty*i))
                break
            else:
                break
        

        tx = -1
        ty = 1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(x + tx*i,y) == False:
                break
            if Board.isNone(x + tx*i,y):
                list_of_moves.append((x + tx*i,y))
            elif Board.isSameColor(x,y,x + tx*i,y) == False:
                list_of_moves.append((x + tx*i,y))
                break
            else:
                break
        
        tx = -1
        ty = 1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(x,y + ty*i) == False:
                break
            if Board.isNone(x,y + ty*i):
                list_of_moves.append((x,y + ty*i))
            elif Board.isSameColor(x,y,x,y + ty*i) == False:
                list_of_moves.append((x,y + ty*i))
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

    def moves(self,x,y):
        list_of_moves = []
        tx = 1
        ty = 1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(x + tx*i,y + ty*i) == False:
                break
            if Board.isNone(x + tx*i,y + ty*i):
                list_of_moves.append((x + tx*i,y + ty*i))
            elif Board.isSameColor(x,y,x + tx*i,y + ty*i) == False:
                list_of_moves.append((x + tx*i,y + ty*i))
                break
            else:
                break
        
        tx = 1
        ty = -1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(x + tx*i,y + ty*i) == False:
                break
            if Board.isNone(x + tx*i,y + ty*i):
                list_of_moves.append((x + tx*i,y + ty*i))
            elif Board.isSameColor(x,y,x + tx*i,y + ty*i) == False:
                list_of_moves.append((x + tx*i,y + ty*i))
                break
            else:
                break
        

        tx = -1
        ty = 1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(x + tx*i,y + ty*i) == False:
                break
            if Board.isNone(x + tx*i,y + ty*i):
                list_of_moves.append((x + tx*i,y + ty*i))
            elif Board.isSameColor(x,y,x + tx*i,y + ty*i) == False:
                list_of_moves.append((x + tx*i,y + ty*i))
                break
            else:
                break
        
        tx = -1
        ty = -1
        for i in range(1,gc.BOX_COUNT_PER_SIDE):
            if Board.isInboard(x + tx*i,y + ty*i) == False:
                break
            if Board.isNone(x + tx*i,y + ty*i):
                list_of_moves.append((x + tx*i,y + ty*i))
            elif Board.isSameColor(x,y,x + tx*i,y + ty*i) == False:
                list_of_moves.append((x + tx*i,y + ty*i))
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

    def moves(self,x,y):
        list_of_moves = []

        if Board.isInboard(x + 1,y + 2) == True and Board.isSameColor(x,y,x + 1,y + 2) == False:
            list_of_moves.append((x + 1,y + 2))
        
        if Board.isInboard(x + 1,y - 2) == True and Board.isSameColor(x,y,x + 1,y - 2) == False:
            list_of_moves.append((x + 1,y - 2))
        
        if Board.isInboard(x - 1,y + 2) == True and Board.isSameColor(x,y,x - 1,y + 2) == False:
            list_of_moves.append((x - 1,y + 2))
        
        if Board.isInboard(x - 1,y - 2) == True and Board.isSameColor(x,y,x - 1,y - 2) == False:
            list_of_moves.append((x - 1,y - 2))
        
        if Board.isInboard(x + 2,y + 1) == True and Board.isSameColor(x,y,x + 2,y + 1) == False:
            list_of_moves.append((x + 2,y + 1))
        
        if Board.isInboard(x + 2,y - 1) == True and Board.isSameColor(x,y,x + 2,y - 1) == False:
            list_of_moves.append((x + 2,y - 1))
        
        if Board.isInboard(x - 2,y + 1) == True and Board.isSameColor(x,y,x - 2,y + 1) == False:
            list_of_moves.append((x - 2,y + 1))
        
        if Board.isInboard(x - 2,y - 1) == True and Board.isSameColor(x,y,x - 2,y - 1) == False:
            list_of_moves.append((x - 2,y - 1))
        
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

    def moves(self,x,y):
        list_of_moves = []
        if ((x - 1) >= 0):
            if Board.isPiece(x - 1,y) == False:
                list_of_moves.append((x - 1,y))
                if((x - 2) >= 0):
                    if Board.isPiece(x - 2,y) == False:
                        list_of_moves.append((x - 2,y))
            
            if (y + 1) < gc.BOX_COUNT_PER_SIDE:
                if Board.isPiece(x - 1,y + 1) == True and Board.isSameColor(x,y,x - 1,y + 1) == False:
                    list_of_moves.append((x - 1,y + 1))
            
            if((y - 1) >= 0) and Board.isSameColor(x,y,x - 1,y - 1) == False:
                if Board.isPiece(x - 1, y - 1) == True:
                    list_of_moves.append((x - 1,y - 1))
        return list_of_moves
