import pygame
from random import choice
from PIL import Image
import os

pygame.init()

screen_height=1000
screen_width=1500

screen=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Egyptian Rat Screw')

clock = pygame.time.Clock()
dt = 0

#load card images at start of game
cardImages=[]
def loadCardImages():
    files = []
    for file in os.listdir(".\cards"):
        files.append(os.path.join(".\cards", file))
    files.sort()

    for file in files:
        pil_image = Image.open(file)
        rimage = pil_image.resize((int(pil_image.size[0]/2), int(pil_image.size[1]/2)))
        card_image = pygame.image.fromstring(rimage.tobytes(), rimage.size, rimage.mode)
        cardImages.append(card_image)

loadCardImages()

# finds card images inside the global array above
def getImage(suit, value):
    pointer=0
    pointer+=((value-1)*4)
    if suit=="clubs":
        pointer+=0
    elif suit=="diamonds":
        pointer+=1
    elif suit=="hearts":
        pointer+=2
    elif suit=="spades":
        pointer+=3
    return cardImages[pointer]



class Card:
    """A model for a typical playing card"""

    def __init__(self, suit, value, face_up=True):
        self.suit=suit
        self.value=value
        self.face_up=face_up
        self.image=getImage(suit, value)
        self.rect=rect()

    def flip(self):
        self.face_up=(not self.face_up)

    def describe(self):
        return f'{self.value} of {self.suit}'
    
    def setpos(self, x, y):
        self.rect=rect(x,y)



class CardDeck:
    """A model for a deck of cards"""

    def __init__(self, empty=False):
        self.empty=empty
        self.deck=[]

        count=0
        if self.empty==False:
            while count<13:
                self.deck.append(Card('spades', count+1))
                count+=1
            while count<26:
                self.deck.append(Card('clubs', (count%13)+1))
                count+=1
            while count<39:
                self.deck.append(Card('hearts', (count%13)+1))
                count+=1
            while count<52:
                self.deck.append(Card('diamonds', (count%13)+1))
                count+=1

    def shuffle(self):
        new_deck=[]
        while self.deck:
            card=choice(self.deck)
            new_deck.append(card)
            self.deck.remove(card)
        self.deck=new_deck
    
    def describe(self):
        for card in self.deck:
            print(card.describe())
    
    def draw_card(self):
        return self.deck.pop()

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


myDeck=CardDeck()
myDeck.shuffle()
testcard=myDeck.deck[5]
card_pos = pygame.Vector2(testcard.rect.x,testcard.rect.y)

running = True
while running:

    screen.fill((20, 20, 100))
    screen.blit(testcard.image, (650, 300))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos # coordinate pair of the click
            print ("clicked at:", mouse_pos)
            rect = testcard.get_rect().move(card_pos)
            if rect.collidepoint(mouse_pos):
                print('clicked on CARD')
            else: print ('clicked on NOTHING')


    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()