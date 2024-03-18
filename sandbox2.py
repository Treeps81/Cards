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
    for file in os.listdir("./cards"):
        files.append(os.path.join("./cards", file))
    files.sort()

    for file in files:
        pil_image = Image.open(file)
        rimage = pil_image.resize((int(pil_image.size[0]/2), int(pil_image.size[1]/2)))
        card_image = pygame.image.fromstring(rimage.tobytes(), rimage.size, rimage.mode)
        cardImages.append(card_image)

loadCardImages()

# finds card images inside the global array above
def getImage(suit, value, face_up):
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
    if face_up==False:
        pointer=52
    return cardImages[pointer]


class Card:
    """A model for a typical playing card"""

    def __init__(self, suit, value, face_up=True):
        self.suit=suit
        self.value=value
        self.face_up=face_up
        self.image=getImage(suit, value, face_up)

    def flip(self, up):
        self.face_up=up
        self.image=getImage(self.suit, self.value, self.face_up)

    def describe(self):
        return f'{self.value} of {self.suit}'
    

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
            playingcard=choice(self.deck)
            new_deck.append(playingcard)
            self.deck.remove(playingcard)
        self.deck=new_deck
    
    def describe(self):
        for playingcard in self.deck:
            print(playingcard.describe())
    
    def draw_card(self):
        return self.deck.pop()



class World:
    """Model of the world"""
    def __init__(self):
        # we start with an empty centerDeck
        # and player has all shuffled cards, face down
        self.centerDeck = CardDeck(True)
        self.player1Deck = CardDeck()
        self.player1Deck.shuffle()
        for carte in self.player1Deck.deck:
            carte.flip(False)
        # add more players here later

        
model = World() # create two decks.
running = True
for playingcard in model.player1Deck.deck:
    playingcard.face_up=False
centerDeck_pos = (650, 100)
playerDeck_pos = (650, 550)

while running:

    # Draw the entire state of the world.
    screen.fill((20, 20, 100)) # cover the screen in purple
    if model.centerDeck.deck:
        topcard = model.centerDeck.deck[-1]
        screen.blit(topcard.image, centerDeck_pos)
    if model.player1Deck.deck:
        topcard = model.player1Deck.deck[-1]
        screen.blit(topcard.image, playerDeck_pos)         
    pygame.display.flip() # show everything we just drew
    dt = clock.tick(60) / 1000 # advance the animation clock

    # Check for events, and respond to them.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # user killed window
            running=False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos # coordinate pair of the click
            #print ("clicked at:", mouse_pos)
            #model.centerDeck.describe()

            if model.centerDeck.deck:
                topcard = model.centerDeck.deck[-1]
                rect = topcard.image.get_rect().move(centerDeck_pos)
                
                
                print(type(model.centerDeck.deck[-1]))
                if rect.collidepoint(mouse_pos) and len(model.centerDeck.deck)>1 and topcard.value==model.centerDeck.deck[-2].value:
                        #print(type(model.centerDeck.deck[-2]))
                        # move the entire center pile back to player deck
                        for i in range(len(model.centerDeck.deck)):
                            topcard=model.centerDeck.deck.pop(0)
                            topcard.flip(False)
                            model.player1Deck.deck.insert(0, topcard)
                
                if rect.collidepoint(mouse_pos) and len(model.centerDeck.deck)>2 and topcard.value==model.centerDeck.deck[-3].value:
                        #print(type(model.centerDeck.deck[-3]))
                        # move the entire center pile back to player deck
                        for i in range(len(model.centerDeck.deck)):
                            topcard=model.centerDeck.deck.pop(0)
                            topcard.flip(False)
                            model.player1Deck.deck.insert(0, topcard)
                elif rect.collidepoint(mouse_pos):
                    model.centerDeck.deck.insert(0, model.player1Deck.draw_card())
                    print('BURN')

            if model.player1Deck.deck:
                topcard = model.player1Deck.deck[-1]
                rect = topcard.image.get_rect().move((playerDeck_pos))
                if rect.collidepoint(mouse_pos):
                    # move the player's top card to the center deck.
                    topcard = model.player1Deck.draw_card()
                    topcard.flip(True)
                    model.centerDeck.deck.append(topcard)
                    print ("added to center: ", topcard.describe())
                    


pygame.quit()