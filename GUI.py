import pygame
import game_config as gc
import Board
import Game as gm
from pygame import display, event, image, Surface, draw, transform

pygame.init()

display.set_caption('CHESS')

screen = display.set_mode((gc.SCREEN_SIZE_X,gc.SCREEN_SIZE_Y))

screen.fill(gc.WHITE)

temp_board = Board.board

def displayChessBoard():
    for row in range(gc.BOX_COUNT_PER_SIDE):
        color = []
        if row%2 == 0:
            color.append(gc.DRAK_BROWN)
            color.append(gc.LIGHT_BROWN)
        else:
            color.append(gc.LIGHT_BROWN)
            color.append(gc.DRAK_BROWN)
        for col in range(gc.BOX_COUNT_PER_SIDE):
            starting_x_of_box = row*gc.BOX_SIDE_LENGTH + gc.SCREEN_MARGIN_SIDE
            starting_y_of_box = col*gc.BOX_SIDE_LENGTH + gc.SCREEN_MARGIN_TOP
            
            draw.rect(screen,color[col%2],(starting_x_of_box,starting_y_of_box,gc.BOX_SIDE_LENGTH,gc.BOX_SIDE_LENGTH))

def displayCurrentStatusBoard(temp_board):
    for row in range(gc.BOX_COUNT_PER_SIDE):
        for col in range(gc.BOX_COUNT_PER_SIDE):
            cur = Board.getPiece(row,col)
            if cur != '.':
                name_of_piece = gc.piece_file_name[cur]
                path_of_piece = 'Chess_Piece/' + name_of_piece
                image_of_piece = image.load(path_of_piece)
                image_of_piece = transform.scale(image_of_piece,(gc.BOX_SIDE_LENGTH,gc.BOX_SIDE_LENGTH))
                
                starting_x_of_box = col*gc.BOX_SIDE_LENGTH + gc.SCREEN_MARGIN_SIDE
                starting_y_of_box = row*gc.BOX_SIDE_LENGTH + gc.SCREEN_MARGIN_TOP

                screen.blit(image_of_piece,(starting_x_of_box,starting_y_of_box))
            

def displayMoves(moves):
    dot_image = image.load('Other/dot.png').convert_alpha()
    margin = 20
    dot_image = transform.scale(dot_image,(gc.BOX_SIDE_LENGTH - 2*margin,gc.BOX_SIDE_LENGTH - 2*margin))
    for x,y in moves:
        starting_x_of_box = y*gc.BOX_SIDE_LENGTH + gc.SCREEN_MARGIN_SIDE + margin
        starting_y_of_box = x*gc.BOX_SIDE_LENGTH + gc.SCREEN_MARGIN_TOP + margin
        screen.blit(dot_image,(starting_x_of_box,starting_y_of_box))


def pawnPromotionScreen():
    running = True

    while running:
        current_event = event.get()
        draw.rect(screen,gc.GREEN,(gc.PROMOTION_SCREEN_OFFSET_X,gc.PROMOTION_SCREEN_OFFSET_Y,gc.PROMOTION_SCREEN_LENGTH,gc.PROMOTION_SCREEN_WIDTH))
        list_of_piece = ["Queen","Rook","Bishop","Knight"]
        for i,piece in enumerate(list_of_piece):
            image_path = 'Chess_Piece/' + gc.GAME_COLOR + '_' + piece + '.png'
            image_of_piece = image.load(image_path)
            image_of_piece = transform.scale(image_of_piece,(gc.PROMOTION_BOX_LENGTH,gc.PROMOTION_BOX_LENGTH))
            screen.blit(image_of_piece,(gc.PROMOTION_SCREEN_OFFSET_X + i*(gc.PROMOTION_FULL_BOX_LENGTH),gc.PROMOTION_SCREEN_OFFSET_Y))

        for e in current_event:
            if e.type == pygame.QUIT:
                running = False
                exit()

            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                x_coordinate = (mouse_x - gc.PROMOTION_SCREEN_OFFSET_X) // gc.PROMOTION_FULL_BOX_LENGTH
                y_coordinate = (mouse_y - gc.PROMOTION_SCREEN_OFFSET_Y)
                if y_coordinate >= 0 and y_coordinate <= gc.PROMOTION_FULL_BOX_LENGTH:
                    if x_coordinate >= 0 and x_coordinate <=3:
                        return list_of_piece[x_coordinate]

        display.flip()
    

def displayScreen():
    running = True

    moves = []

    selected = False

    selected_piece_row = -1
    selected_piece_col = -1

    while running:
        current_event = event.get()

        displayChessBoard()

        displayCurrentStatusBoard(temp_board)
        
        for e in current_event:
            if e.type == pygame.QUIT:
                running = False

            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                row = (mouse_y - gc.SCREEN_MARGIN_TOP) // gc.BOX_SIDE_LENGTH
                col = (mouse_x - gc.SCREEN_MARGIN_SIDE) // gc.BOX_SIDE_LENGTH
                if selected == False:
                    if Board.isPiece(row,col):
                        selected = True
                        selected_piece_row = row
                        selected_piece_col = col
                        moves = Board.getMoves(row,col)
                else:
                    notation = Board.getPiece(selected_piece_row,selected_piece_col)
                    if (notation[1] == 'P'):
                        if(row == 0):
                            gm.pawnPromotion(selected_piece_row,selected_piece_col,row,col,pawnPromotionScreen())
                        else:
                            gm.moveOnBoard(selected_piece_row,selected_piece_col,row,col)
                    else:
                        gm.moveOnBoard(selected_piece_row,selected_piece_col,row,col)
                    selected = False
                    moves = []

        displayMoves(moves)

        display.flip()
        pygame.time.wait(1)