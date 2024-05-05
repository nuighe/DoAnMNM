import pygame
from fighter import Fighter
from pygame import mixer

mixer.init()
pygame.init()

class MenuOnline():
    def __init__(self):
        self.SCREEN_W = 1000
        self.SCREEN_H = 600
        self.ft = "a"
        self.ft2 = "a"
        self.ready1 = "Choosing"
        self.ready2 = "Choosing"
        self.map = 1
        self.FPS = 60
        self.run = True
        self.intro_count = 3
        self.text_font = pygame.font.Font("assets/fonts/emulogic.ttf", 30)
        self.screen = pygame.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        self.menu_image = pygame.image.load("assets/images/background/menuOffline.jpg").convert_alpha()
        self.map1_image = pygame.image.load("assets/images/background/desert.jfif").convert_alpha()
        self.map2_image = pygame.image.load("assets/images/background/football.jfif").convert_alpha()
        self.map3_image = pygame.image.load("assets/images/background/hill.jfif").convert_alpha()
        self.vs_image = pygame.image.load("assets/images/icons/vs.png").convert_alpha()

        #define fighter variables
        WARRIOR_SIZE = 162
        WARRIOR_SCALE = 4
        WARRIOR_OFFSET = [72, 56]
        WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
        WIZARD_SIZE = 250
        WIZARD_SCALE = 3
        WIZARD_OFFSET = [112, 107]
        WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]
        HUTRESS_SIZE = 150
        HUTRESS_SCALE = 4
        HUTRESS_OFFSET = [66, 52]
        HUTRESS_DATA = [HUTRESS_SIZE, HUTRESS_SCALE, HUTRESS_OFFSET]

        #define number of steps in each animation
        WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
        WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]
        HUTRESS_ANIMATION_STEPS = [8, 8, 2, 5, 5, 3, 8]

        #load spritesheets
        warrior_sheet = pygame.image.load("assets/images/warrior/Sprites/warrior.png").convert_alpha()
        wizard_sheet = pygame.image.load("assets/images/wizard/Sprites/wizard.png").convert_alpha()
        huntress_sheet = pygame.image.load("assets/images/huntress/Sprites/huntress.png").convert_alpha()

        #load music and sounds
        pygame.mixer.music.load("assets/audio/music.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1, 0.0, 5000)
        sword_fx = pygame.mixer.Sound("assets/audio/sword.wav")
        sword_fx.set_volume(0.5)
        magic_fx = pygame.mixer.Sound("assets/audio/magic.wav")
        magic_fx.set_volume(0.75)

        #create two instances of fighters
        self.fighter_1 = Fighter(1, 150, 250, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
        self.fighter_2 = Fighter(1, 150, 250, False, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)
        self.fighter_3 = Fighter(1, 150, 250, False, HUTRESS_DATA, huntress_sheet, HUTRESS_ANIMATION_STEPS, sword_fx)

        self.fighter_a = Fighter(1, 750, 250, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
        self.fighter_b = Fighter(1, 750, 250, False, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)
        self.fighter_c = Fighter(1, 750, 250, False, HUTRESS_DATA, huntress_sheet, HUTRESS_ANIMATION_STEPS, sword_fx)

    #function for drawing menu
    def draw_menu(self):
        scaled_menu = pygame.transform.scale(self.menu_image, (self.SCREEN_W, self.SCREEN_H))
        self.screen.blit(scaled_menu, (0, 0))
        scaled_vs = pygame.transform.scale(self.vs_image, (self.SCREEN_W/4, self.SCREEN_H/4))
        self.screen.blit(scaled_vs, (350, 250))
        if self.map == 1:
            scaled_map1 = pygame.transform.scale(self.map1_image, (self.SCREEN_W/4, self.SCREEN_H/4))
            self.screen.blit(scaled_map1, (370, 50))
        elif self.map == 2:
            scaled_map2 = pygame.transform.scale(self.map2_image, (self.SCREEN_W/4, self.SCREEN_H/4))
            self.screen.blit(scaled_map2, (370, 50))
        elif self.map == 3:
            scaled_map3 = pygame.transform.scale(self.map3_image, (self.SCREEN_W/4, self.SCREEN_H/4))
            self.screen.blit(scaled_map3, (370, 50))

    def draw_fighter(self, ft, ft2):
        if ft == "a":
            self.fighter_1.update()
            self.fighter_1.draw(self.screen)
        elif ft == "b":
            self.fighter_2.update()
            self.fighter_2.draw(self.screen)
        elif ft == "c":
            self.fighter_3.update()
            self.fighter_3.draw(self.screen)
        if ft2 == "a":
            self.fighter_a.update()
            self.fighter_a.draw(self.screen)
        elif ft2 == "b":
            self.fighter_b.update()
            self.fighter_b.draw(self.screen)
        elif ft2 == "c":
            self.fighter_c.update()
            self.fighter_c.draw(self.screen)

    def createMenu(self, client):
        while self.run:

            #draw menu
            self.draw_menu()

            milliseconds = pygame.time.get_ticks()
            if milliseconds // 1000 % 2 == 0:
                text_surface = self.text_font.render("Press Enter To Ready", True, (255, 255, 255))  # Màu trắng
            else:
                text_surface = self.text_font.render("", True, (255, 255, 255))  # Màu trắng 
            self.screen.blit(text_surface, (self.SCREEN_W - self.SCREEN_W * 0.8, self.SCREEN_H - self.SCREEN_H * 0.1))

            if milliseconds // 100 % 2 == 0:
                text_ready = self.text_font.render(self.ready1, True, (255, 255, 255))  # Màu trắng
            elif self.ready1 == "Choosing":
                text_ready = self.text_font.render("", True, (255, 255, 255))  # Màu trắng 
            self.screen.blit(text_ready, (self.SCREEN_W - self.SCREEN_W * 0.9, self.SCREEN_H - self.SCREEN_H * 0.2))

            if milliseconds // 100 % 2 == 0:
                text_ready2 = self.text_font.render(self.ready2, True, (255, 255, 255))  # Màu trắng
            elif self.ready2 == "Choosing":
                text_ready2 = self.text_font.render("", True, (255, 255, 255))  # Màu trắng 
            self.screen.blit(text_ready2, (self.SCREEN_W - self.SCREEN_W * 0.3, self.SCREEN_H - self.SCREEN_H * 0.2))


            text_p1 = self.text_font.render("P1", True, (255, 255, 255))
            text_p2 = self.text_font.render("P2", True, (255, 255, 255))
            self.screen.blit(text_p1, (self.SCREEN_W - self.SCREEN_W * 0.9, self.SCREEN_H - self.SCREEN_H * 0.9))
            self.screen.blit(text_p2, (self.SCREEN_W - self.SCREEN_W * 0.3, self.SCREEN_H - self.SCREEN_H * 0.9))

            text_wa = self.text_font.render("Warrior", True, (255, 255, 255))
            text_wi = self.text_font.render("Wizzar", True, (255, 255, 255))
            text_hu = self.text_font.render("Huntress", True, (255, 255, 255))
            if self.ft == "a":
                self.screen.blit(text_wa, (self.SCREEN_W - self.SCREEN_W * 0.9, self.SCREEN_H - self.SCREEN_H * 0.8))
            elif self.ft == "b":
                self.screen.blit(text_wi, (self.SCREEN_W - self.SCREEN_W * 0.9, self.SCREEN_H - self.SCREEN_H * 0.8))
            elif self.ft == "c":
                self.screen.blit(text_hu, (self.SCREEN_W - self.SCREEN_W * 0.9, self.SCREEN_H - self.SCREEN_H * 0.8))

            if self.ft2 == "a":
                self.screen.blit(text_wa, (self.SCREEN_W - self.SCREEN_W * 0.3, self.SCREEN_H - self.SCREEN_H * 0.8))
            elif self.ft2 == "b":
                self.screen.blit(text_wi, (self.SCREEN_W - self.SCREEN_W * 0.3, self.SCREEN_H - self.SCREEN_H * 0.8))
            elif self.ft2 == "c":
                self.screen.blit(text_hu, (self.SCREEN_W - self.SCREEN_W * 0.3, self.SCREEN_H - self.SCREEN_H * 0.8))
 
            self.draw_fighter(self.ft, self.ft2)

            #event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.ready1 = "Ready"
                        client.send("Ready")
                    elif event.key == pygame.K_a and self.ft == "a" and self.ready1 != "Ready":
                        self.ft = "b"
                        client.send(self.ft)
                    elif event.key == pygame.K_a and self.ft == "b" and self.ready1 != "Ready":
                        self.ft = "c"
                        client.send(self.ft)
                    elif event.key == pygame.K_d and self.ft =="b" and self.ready1 != "Ready":
                        self.ft = "a" 
                        client.send(self.ft)
                    elif event.key == pygame.K_d and self.ft =="c" and self.ready1 != "Ready":
                        self.ft = "b" 
                        client.send(self.ft)
                    elif event.key == pygame.K_SPACE and self.map != 3: 
                        self.map = self.map + 1       
                    elif event.key == pygame.K_SPACE and self.map == 3: 
                        self.map = 1  

            if self.ready1 == "Ready" and self.ready2 == "Ready":
                break   

            try:
                temp = client.clientsocket.recv(1024).decode(client.FORMAT)
                if temp == "a" or temp == "b" or temp == "c":
                    self.ft2 = temp
                elif temp == "Ready" or temp == "Choosing":
                    self.ready2 = temp
            except Exception as e:
                pass   

            #update display
            pygame.display.update()
        if self.ft == "a":
            self.ft = 1
        if self.ft == "b":
            self.ft = 2
        if self.ft == "c":
            self.ft = 3
        if self.ft2 == "a":
            self.ft2 = 1
        if self.ft2 == "b":
            self.ft2 = 2
        if self.ft2 == "c":
            self.ft2 = 3
        return self.ft, self.ft2, self.map



