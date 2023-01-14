import pygame as pg
pg.init()

#SİMİLASYON PENÇERESİNİN YAPILMASI
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 750

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Ohm kanunu")


#SİMİLASYON DEĞİŞKENLERİ
game_paused = False
menu_state = "main"
volt = 10
r1= 5
r2 = 5
r3 = 5
rtoplam = 5.40
Circuit_State= 1
Akımson = 1.85

#YAZI FONTUNUN TANIMLANMASI
font_15 = pg.font.SysFont("arialblack", 15)
font_25 = pg.font.SysFont("arialblack", 25)
font_20 = pg.font.SysFont("arial",20)

#RENKLERİN TANIMLANMASI
WHITE_RGB = (255, 255, 255)
BLACK_RGB= (0,0,0)

#DİRENÇ RESİMLERİNİN YÜKLENMESİ
direnc = pg.image.load("Direnc.png")
devre_img1 = pg.image.load("PS.png").convert_alpha()
devre_img2 = pg.image.load("paralel.png").convert_alpha()
devre_img3 = pg.image.load("seri.png").convert_alpha()
devre_img = devre_img1

#BUTON RESİMLERİNİN YÜKLENMESİ
def dikdörtgen(genislik,yukseklik,x,y): #Dikdörtgen oluşturur

  dikdörtgen_nesnesi = pg.Surface((genislik,yukseklik))
  dikdörtgen_nesnesi.fill((240, 248, 255))
  dikdörtgen_nesnesi_konumu = (x, y)
  
  screen.blit(dikdörtgen_nesnesi, dikdörtgen_nesnesi_konumu)
  
#BUTONUN YÜKLENMESİ
class Button():
  def __init__(self, x, y, image, oran):
	  width = image.get_width()
		height = image.get_height()
		self.image = pg.transform.scale(image, (int(width * oran), int(height * oran)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False  
  def draw(self, surface):
		action = False
		#get mouse position
		pos = pg.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pg.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action 
resume_img = pg.image.load("button_resume.png").convert_alpha()
options_img = pg.image.load("button_options.png").convert_alpha()
quit_img = pg.image.load("button_quit.png").convert_alpha()
  

