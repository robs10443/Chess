import Pieces

class Board:
    def __init__(self,color):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        
        #intialization of board based on the color
        if color.lower() == "white":
            self.board[0][0] = Pieces.Rook("Black")
            self.board[0][1] = Pieces.Knight("Black")
            self.board[0][2] = Pieces.Bishop("Black")
            self.board[0][3] = Pieces.Queen("Black")
            self.board[0][4] = Pieces.King("Black")
            self.board[0][5] = Pieces.Bishop("Black")
            self.board[0][6] = Pieces.Knight("Black")
            self.board[0][7] = Pieces.Rook("Black")
            
            for x in range(8):
                self.board[1][x] = Pieces.Pawn("Black")
            
            self.board[7][0] = Pieces.Rook("White")
            self.board[7][1] = Pieces.Knight("White")
            self.board[7][2] = Pieces.Bishop("White")
            self.board[7][3] = Pieces.Queen("White")
            self.board[7][4] = Pieces.King("White")
            self.board[7][5] = Pieces.Bishop("White")
            self.board[7][6] = Pieces.Knight("White")
            self.board[7][7] = Pieces.Rook("White")
            
            for x in range(8):
                self.board[6][x] = Pieces.Pawn("White")
            
        else:
            self.board[0][0] = Pieces.Rook("White")
            self.board[0][1] = Pieces.Knight("White")
            self.board[0][2] = Pieces.Bishop("White")
            self.board[0][3] = Pieces.Queen("White")
            self.board[0][4] = Pieces.King("White")
            self.board[0][5] = Pieces.Bishop("White")
            self.board[0][6] = Pieces.Knight("White")
            self.board[0][7] = Pieces.Rook("White")
            
            for x in range(8):
                self.board[1][x] = Pieces.Pawn("White")
            
            self.board[7][0] = Pieces.Rook("Black")
            self.board[7][1] = Pieces.Knight("Black")
            self.board[7][2] = Pieces.Bishop("Black")
            self.board[7][3] = Pieces.Queen("Black")
            self.board[7][4] = Pieces.King("Black")
            self.board[7][5] = Pieces.Bishop("Black")
            self.board[7][6] = Pieces.Knight("Black")
            self.board[7][7] = Pieces.Rook("Black")
            
            for x in range(8):
                self.board[6][x] = Pieces.Pawn("Black")

    def getPiece(self,x,y):
        if self.board[x][y] == None:
            return "."
        return self.board[x][y].getNotation()
    
    def isPiece(self,x,y):
        if self.board[x][y] == None:
            return False
        else:
            return True

    def getMoves(self,x,y):
        if self.board[x][y] == None:
            return []
        return self.board[x][y].Moves(x,y)