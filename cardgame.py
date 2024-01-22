import pygame
from random import choice
from PIL import Image
import os




cardImages=[]
#load card images at start of game
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

def getImage(suit, value):
    pointer=0
    pointer+=((value-1)*4)
    if suit=="clubs":
        pointer+=1
    elif suit=="diamonds":
        pointer+=2
    elif suit=="hearts":
        pointer+=3
    elif suit=="spades":
        pointer+=4
    return cardImages[pointer]


class Card:
    """A model for a typical playing card"""

    def __init__(self, suit, value, face_up=True):
        self.suit=suit
        self.value=value
        self.face_up=face_up
        self.image=getImage(suit, value)

    def flip(self):
        self.face_up=(not self.face_up)

    def describe(self):
        return f'{self.value} of {self.suit}'
    
    def draw(self,x,y):
        self.

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
    
    def check(self):
        pass
        

#my_deck=CardDeck()
#my_deck.shuffle()
#my_deck.__init__()
#y_deck.describe()

#hand=[]
#while True:
    #action=input()
    #if action=='hit me':
      #my_deck.shuffle()
      #played_card=my_deck.draw_card()
      #hand.append(played_card.value)  
      #total=sum(hand)
      #print(total)
    #if total>=22:
        #my_deck.__init__()
        #break

#ERS

#hand=[]
#while True:
    #action=input('Your Move:')
    #if action=='play':
      #my_deck.shuffle()
      #played_card=my_deck.draw_card()
      #hand.append(played_card.value)
      #print(played_card.describe)
    #if action=='q':
        #my_deck.__init__()
        #break
    
