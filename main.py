import Board as brd
import Pieces as pc
import GUI as gui
import game_config as gc
import threading

def initGame(color):
    gc.GAME_COLOR = color
    brd.init(color)
    t1 = threading.Thread(target = callDisplayScreen)
    t1.start()

def callDisplayScreen():
    gui.displayScreen()

initGame("White")