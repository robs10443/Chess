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

    def setLongCastle(self,flag):
        self.long_castle = flag
    
    def setShortCastle(self,flag):
        self.short_castle = flag

    def isLongCastle(self,flag):
        return self.long_castle
    
    def isShortCastle(self,flag):
        return self.short_castle

    def moves(self):
        pass

class Queen:
    def __init__(self,color):
        self.notation = color[0].upper() + "Q"

    def getNotation(self):
        return self.notation

    def moves(self):
        pass

class Rook:
    def __init__(self,color):
        self.notation = color[0].upper() + "R"
        self.is_moved = False

    def getNotation(self):
        return self.notation

    def setIsMoved(self,flag):
        self.is_moved = flag

    def IsMoved(self):
        return self.is_moved

    def moves(self):
        pass

class Bishop:
    def __init__(self,color):
        self.notation = color[0].upper() + "B"
        
    def getNotation(self):
        return self.notation

    def moves(self):
        pass

class Knight:
    def __init__(self,color):
        self.notation = color[0].upper() + "N"
        
    def getNotation(self):
        return self.notation

    def moves(self):
        pass

class Pawn:
    def __init__(self,color):
        self.notation = color[0].upper() + "P"
        self.first_move = False

    def getNotation(self):
        return self.notation

    def isFirstMove(self):
        return self.first_move

    def setFirstMove(self,flag):
        self.first_move = flag

    def moves(self,x,y):
        pass
        # list_of_moves = []
        # if (x + 1) <= 0:
        #     if temp_board.isPiece(x + 1,y) == False:
        #         list_of_moves.append((x + 1,y))
        #         if((x + 2) <= 0):
        #             if temp_board.isPiece(x + 2,y) == False:
        #                 list_of_moves.append((x + 2,y))
            
        #     if (y + 1) <= gc.BOX_COUNT_PER_SIDE:
        #         if temp_board.isPiece(x + 1,y + 1) == True:
        #             list_of_moves.append((x + 1,y + 1))
            
        #     if((y - 1) >= 0):
        #         if temp_board.isPiece(x + 1, y - 1) == False:
        #             list_of_moves.append((x + 1,y - 1))

