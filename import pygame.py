import pygame
from random import choice


class Controller():
    """Game controller for ERS"""

    def __init__(self):
        pass

    def deal(self, number_of_players):
        self.lists=[[] for player in range(number_of_players)]
        count=1
        dealing_deck=CardDeck()
        while dealing_deck.deck:
            self.lists[count%number_of_players].append(dealing_deck.draw_card())
            count+=1

controller=Controller()
#pygame stuff
screen_height=1000
screen_width=1500

screen=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Egyptian Rat Screw')


class Button:
    def __init__(self,x,y,image,scale=1):
        width=image.get_width()
        height=image.get_height()
        self.image=pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False

    def check_clicked(self):
        action=False
        mouse_pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos)==True:
            if pygame.mouse.get_pressed()[0]==True and self.clicked==False:
                self.clicked=True
                action=True
                
        if pygame.mouse.get_pressed()[0]==False:
            self.clicked=False
            action=False
        return action

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


start_image=pygame.image.load('Downloads/start_button.png').convert_alpha()
start_button=Button(620, 700, start_image)





running = True
while running:

    screen.fill((20, 20, 100))

    start_button.draw()
    if start_button.check_clicked==True:
        print('hello')

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False


    pygame.display.update()