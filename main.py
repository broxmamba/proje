import pygame as pygame
import pygame as pg
pygame.init()

#oyun ekrani yaratma
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Ohm kanunu")


#simulasyon degiskenleri
game_paused = False
menu_state = "main"
volt = 10
r1= 5
r2 = 5
r3 = 5
rtoplam = 5.40
Circuit_State= 1
Akımson = 1.85

#font ayarlama
font = pg.font.SysFont("arialblack", 15)
fontd = pg.font.SysFont("arialblack", 25)
fontD = pg.font.SysFont("arial",20)
#renk ayarlama
TEXT_COL = (255, 255, 255)
D_COL = (0,0,0)

direnc = pg.image.load("Direnc.png")
devre_img1 = pg.image.load("PS.png").convert_alpha()
devre_img2 = pg.image.load("paralel.png").convert_alpha()
devre_img3 = pg.image.load("seri.png").convert_alpha()
devre_img = devre_img1
#buton resimlerini yükleme

def dikdörtgen(genislik,yukseklik,x,y):
  #Dikdörtgen oluşturur

  dikdörtgen_nesnesi = pg.Surface((genislik,yukseklik))
  dikdörtgen_nesnesi.fill((240, 245, 255))
  dikdörtgen_nesnesi_konumu = (x, y)
  
  screen.blit(dikdörtgen_nesnesi, dikdörtgen_nesnesi_konumu)

  
  

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
		#mouse konumunu ayarlama
		pos = pg.mouse.get_pos()

		#mouse ve tiklamayi kontrol etme
		if self.rect.collidepoint(pos):
			if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pg.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#ekranda buton cizme
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action 
resume_img = pg.image.load("button_resume.png").convert_alpha()
options_img = pg.image.load("button_options.png").convert_alpha()
quit_img = pg.image.load("button_quit.png").convert_alpha()


#buton ornekleri yaratma
resume_button = Button(440, 125, resume_img, 1)
options_button = Button(440, 250, options_img, 1)
quit_button = Button(440, 375, quit_img, 1)
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))
def direnctoplam(R1,R2,R3):
  global Circuit_State,rtoplam 
  if Circuit_State == 1:
    rtoplam = round(R1+(1/R2)+(1/R3),2)
  elif Circuit_State == 2:
    rtoplam = round((1/R1)+(1/R2)+(1/R3),2)
  elif Circuit_State == 3:
    rtoplam = (R1+R2+R3)
  else: rtoplam = ""
   
def textbox():
    global game_paused,menu_state,r1,r2,r3,Circuit_State,volt,devre_img
    screen = pg.display.set_mode((1080, 720))
    font2 = pg.font.SysFont("arialblack", 25)
    clock = pg.time.Clock()
    input_box = pg.Rect(440, 250, 140, 50)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('White')
    color = color_inactive
    active = False
    text = ''
    done = False
    yazı = ""
    yazı2 = "Voltaj değerini giriniz"
    font_hata = pg.Color("White")
    text_box_state = int(6)
    def text_ayarlar(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (450, y))
    while not done:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
              
                if active:
                    if event.key == pg.K_RETURN:
                      try:
                        sayı = int(text)
                        text_box_state -= 1
                        if text_box_state == 5:
                          yazı2 = "1 Numaralı Direnç (r1)"
                          volt = sayı
                          text = ''
                          print (volt)
                        elif text_box_state == 4:
                          yazı2 = "2 Numaralı Direnç (r2)"
                          r1 = sayı
                          text = ''
                          print (r1)
                        elif text_box_state == 3:
                          yazı2 = "3 Numaralı Direnç (r3)"
                          r2 = sayı
                          text = ''
                          print (r2)
                        elif text_box_state == 2:
                          yazı2 = "Devre Tipi (1- Komplike 2- Paralel 3- Seri)"
                          r3 = sayı
                          text =''
                          print (r3)
                          
                        elif text_box_state == 1:
                          Circuit_State = sayı
                          if 0< Circuit_State < 4:
                            print(Circuit_State)
                            yazı = "Anasayfaya dönmek için Enter'a basın"
                            yazı2 = ""
                            font_hata = pg.Color("White")
                            direnctoplam(r1,r2,r3)
                          else:
                            yazı = "1-2-3 değerlerinden birini girin"
                            text_box_state = 2

                        
                        if text_box_state == 0:
                          
                          game_paused= True
                          done = True
                          menu_state = "main"
                          text_box_state = 4
                          if Circuit_State == 1:
                            devre_img = devre_img1
                          elif Circuit_State == 2:
                            devre_img = devre_img2
                          elif Circuit_State == 3:
                            devre_img = devre_img3
                        break
                      except:
                        yazı = "Lütfen sadece sayı giriniz"
                         
                        
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                          text += event.unicode
            arkaa_plan = pygame.image.load("bulb.png")
            screen.blit(arkaa_plan, (0,0))
        # Render the current text.
        txt_surface = font2.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        text_ayarlar(yazı, font, font_hata, 400, 310)
        text_ayarlar(yazı2, font, font_hata, 400, 225)
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 3)
       
        pg.display.flip()
        clock.tick(30)
#oyun dongusu
run = True
while run:

  arka_plan = pygame.image.load("wallpaperr.png")

  screen.blit(arka_plan, (0,0)) #arkaplan

  #oyun durdurma kontrolleri
  if game_paused == False:
    #check menu state
    if menu_state == "main":
      #draw pause screen buttons
      if resume_button.draw(screen):
        game_paused = True
      if options_button.draw(screen):
        menu_state = "options"

      if quit_button.draw(screen):
        run = False
    #ayarlar menusu kontrolleri
    if menu_state == "options":
      textbox()
      run = True
      
      if quit_button.draw(screen):

        run= False
  else:
    
    dikdörtgen(400,300,30,50)
    dikdörtgen(400,300,30,350)
    screen.blit(devre_img,(0,50))
    screen.blit(direnc,(0,275))
     
    draw_text("Durdurmak için SPACE'e basın", font, TEXT_COL, 5, 5)
    draw_text("Voltaj: {} volt ".format(volt), fontD,D_COL,40,175)
    draw_text("R1: {} Ohm ".format(r1), fontD,D_COL,40,100)
    draw_text("R2: {} Ohm ".format(r2), fontD,D_COL,40,125)
    draw_text("R3: {} Ohm ".format(r3), fontD,D_COL,40,150)
    draw_text("Akım: {} Amper ".format(round(volt/rtoplam,2)), fontd,D_COL,40,200)
    draw_text("Rtoplam: {} Ohm ".format(rtoplam), fontd,D_COL,40,250)
    
    
  
  #etkinlik duzeni
  for event in pg.event.get():
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_SPACE:
        game_paused = False
    if event.type == pg.QUIT:
      run = False

  pg.display.update()

pg.quit()
