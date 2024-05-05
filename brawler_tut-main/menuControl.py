import pygame
from pygame import mixer

mixer.init()
pygame.init()

class MenuControl():
    def __init__(self):
        self.SCREEN_W = 1000
        self.SCREEN_H = 600
        self.status = 1
        self.FPS = 60
        self.run = True
        self.text_font = pygame.font.Font("assets/fonts/emulogic.ttf", 30)
        self.screen = pygame.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        self.menu_image = pygame.image.load("assets/images/background/menu.jpg").convert_alpha()
        self.online_image = pygame.image.load("assets/images/icons/online.png").convert_alpha()
        self.offline_image = pygame.image.load("assets/images/icons/offline.png").convert_alpha()

    #function for drawing menu
    def draw_menu(self):
        scaled_menu = pygame.transform.scale(self.menu_image, (self.SCREEN_W, self.SCREEN_H))
        self.screen.blit(scaled_menu, (0, 0))

    def createMenu(self):
        while self.run:

            #draw menu
            self.draw_menu()

            milliseconds = pygame.time.get_ticks()
            if milliseconds // 1000 % 2 == 0:
                text_surface = self.text_font.render("Press Enter To Start", True, (255, 255, 255))  # Màu trắng
            else:
                text_surface = self.text_font.render("", True, (255, 255, 255))  # Màu trắng 
            self.screen.blit(text_surface, (self.SCREEN_W - self.SCREEN_W * 0.8, self.SCREEN_H - self.SCREEN_H * 0.15))

            #event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.run = False
                    elif event.key == pygame.K_LEFT and self.status > 1:
                        self.status = self.status - 1
                    elif event.key == pygame.K_RIGHT and self.status < 2:
                        self.status = self.status + 1                        

            if self.status == 1:
                scaled_online = pygame.transform.scale(self.online_image, (200, 50))
                self.screen.blit(scaled_online, (self.SCREEN_W *0.4, self.SCREEN_H*0.7))
            else:
                scaled_offline = pygame.transform.scale(self.offline_image, (200, 50))
                self.screen.blit(scaled_offline, (self.SCREEN_W *0.4, self.SCREEN_H*0.7))

            #update display
            pygame.display.update()


        return self.status



