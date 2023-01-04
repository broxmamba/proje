import pygame as pg
pg.init()

#create game window
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 750

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Ohm kanunu")


#game variables
game_paused = False
menu_state = "main"
volt = 10
r1= 5
r2 = 5
r3 = 5
rtoplam = 5.40
Circuit_State= 1
Akımson = 1.85

#define fonts
font = pg.font.SysFont("arialblack", 15)
fontd = pg.font.SysFont("arialblack", 25)
fontD = pg.font.SysFont("arial",20)
#define colours
TEXT_COL = (255, 255, 255)
D_COL = (0,0,0)