from data import *
from images import Image

class Character:
    def __init__(self,name,weaknesses,image,player):
        super().__init__()
        self.points = 0
        self.name = name
        self.weaknesses = weaknesses
        self.player = player
        self.last_word = "not_defined"
        self.end_sentence = False
        self.own_turn = 0
        self.my_awful_sentence = []
        if self.player == 1 : 
            self.image = Image(image, 30, 180)
        if self.player == 2 : 
            self.image = Image(image, 740, 180)

    def update_scorebar(self, surface):
        #affichage du score du joueur durant le combat
        bar_color = (219, 72, 72)
        bar_position = [self.image.rect.x + 10, self.image.rect.y -20, self.points, 20]     
        pygame.draw.rect(surface, bar_color, bar_position)