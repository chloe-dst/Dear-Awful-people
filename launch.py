from images import Image
from data import *
from math import floor

class Launch : 

    def __init__(self): 
        self.is_playing = True
        #creer les différents backgrounds
        self.Background1 = Image(background1, 0, 0)
        self.Background2 = Image(background2, 0, 0)
        self.Background3 = Image(background3, 0, 0)
        self.Background4 = Image(background4, 0, 0)
        self.Background5 = Image(background5, 0, 0)
        self.Background_bibliotheque = Image(background_bibliotheque,0,0)
        self.Background_entree = Image(background_entree,0,0)
        self.Background_petitsalon = Image(background_petitsalon,0,0)
        self.Background_jardin = Image(background_jardin,0,0)
        self.Background_salleamanger = Image(background_salleamanger,0,0)
        #creer les différents boutons
        self.button_menu = Image(button1,405,450) 
        self.button_consignes = Image(button2,780,610)
        self.button_bibliotheque = Image(buttonbiblio,610,400)
        self.button_entree = Image(buttonentree,170,550)
        self.button_petitsalon = Image(buttonsalon,630,550)
        self.button_jardin_locked = Image(buttonjardin_locked,820,530)
        self.button_salleamanger_locked = Image(buttonsalleamanger_locked,125,400)
        self.button_jardin_unlocked = Image(buttonjardin_unlocked,820,530)
        self.button_salleamanger_unlocked = Image(buttonsalleamanger_unlocked,125,400)
        self.choix_perso1 = Image(choixperso1, 30, 200)
        self.choix_perso2 = Image(choixperso2, 286, 200)
        self.choix_perso3 = Image(choixperso3, 544, 200)
        self.choix_perso4 = Image(choixperso4, 800, 200)
        self.button_retourmenu = Image(retourmenu, 410,635)
        #importer les éléments graphiques du lancement du jeu
        self.backgrounds_sprites = pygame.sprite.Group()
        self.backgrounds_sprites.add(self.Background1)
        self.buttons_sprites = pygame.sprite.Group()
        self.buttons_sprites.add(self.button_menu)
        # créer les éléments du combat
        self.p1_dialogue_bubble = Image(p1_dialogue_bubble, 100, 20)
        self.p1_turn_signal = Image(p1_turn_signal, 35, 440)
        self.p1_end_sentence_button = Image(p1_end_sentence_button, 260, 670)
        self.p2_dialogue_bubble = Image(p2_dialogue_bubble, 150, 20)
        self.p2_turn_signal = Image(p2_turn_signal, 1005, 440)
        self.p2_end_sentence_button = Image(p2_end_sentence_button, 755, 670)
        self.p1_banner_1 = Image(p1_banner_1, 765, 520)
        self.p2_banner_1 = Image(p2_banner_1, 20, 520)
        self.p1_banner_2 = Image(p1_banner_2, 780, 520)
        self.p2_banner_2 = Image(p2_banner_2, 50, 520)
        self.swearing_letter = Image(swearing_letter, 340, 190)
        self.combat_group_sprite = pygame.sprite.Group()
        self.combat_group_sprite.add(self.swearing_letter)

    def start(self,fight):
        #fonction pour revenir au choix des lieux 
        self.is_playing = True
        self.backgrounds_sprites.add(self.Background5)
        self.buttons_sprites.add(self.button_bibliotheque)
        self.buttons_sprites.add(self.button_petitsalon)
        self.buttons_sprites.add(self.button_entree)
        self.buttons_sprites.add(self.button_jardin_locked)
        self.buttons_sprites.add(self.button_salleamanger_locked)
        #remplace boutons sans cadenas et les rend cliquables 
        if fight.level_jardin == True :
            self.buttons_sprites.remove(self.button_jardin_locked)
            self.buttons_sprites.add(self.button_jardin_unlocked)
        if fight.level_salleamanger == True :
            self.buttons_sprites.remove(self.button_salleamanger_locked)
            self.buttons_sprites.add(self.button_salleamanger_unlocked)

    def end(self,fight,surface,menu,p1,p2):
        #fonction pour passer du choix des lieux au lieu de combat 
        self.is_playing = False
        fight.level = "vide"
        self.backgrounds_sprites.remove(self.Background5) 
        self.buttons_sprites.remove(self.button_bibliotheque)
        self.buttons_sprites.remove(self.button_entree)
        self.buttons_sprites.remove(self.button_petitsalon)
        self.buttons_sprites.remove(self.button_jardin_locked)
        self.buttons_sprites.remove(self.button_salleamanger_locked) 
        self.buttons_sprites.remove(self.button_jardin_unlocked)
        self.buttons_sprites.remove(self.button_salleamanger_unlocked)
        self.combat_group_sprite.remove(self.p2_dialogue_bubble)
        self.combat_group_sprite.remove(self.p1_dialogue_bubble)
        self.combat_group_sprite.remove(menu.p1_turn_signal)
        self.combat_group_sprite.remove(menu.p2_turn_signal)
        fight.start(surface,menu,p1,p2)
    
    def parties_played(self,fight): 
        #affiche le nombre de parties jouées
        fond = pygame.Surface((330,60))
        fond.fill((255,255,255))
        displaysurface.blit(fond, (700,145)) 
        font = pygame.font.Font("assets/Montserrat-Regular.ttf", 24)
        partiesjouees_text = font.render(f"Parties jouées : {fight.nb_parties}", 1, (42,111,120))
        displaysurface.blit(partiesjouees_text, (760,160))

    def visibility_object_fight_p1(self) :
        # Quand c'est le tour de de p1 de jouer
        self.combat_group_sprite.remove(self.p2_end_sentence_button)
        self.combat_group_sprite.remove(self.p2_dialogue_bubble)
        self.combat_group_sprite.remove(self.p2_turn_signal)
        self.combat_group_sprite.remove(self.p1_banner_1)
        self.combat_group_sprite.remove(self.p2_banner_2)
        self.combat_group_sprite.remove(self.p2_banner_1)
        self.combat_group_sprite.remove(self.p1_banner_2)

        self.combat_group_sprite.add(self.p1_end_sentence_button)
        self.combat_group_sprite.add(self.p1_dialogue_bubble)
        self.combat_group_sprite.add(self.p1_turn_signal)

    def visibility_object_fight_p2(self) :
        # Quand c'est le tour de p2 de jouer
        self.combat_group_sprite.remove(self.p1_end_sentence_button)
        self.combat_group_sprite.remove(self.p1_dialogue_bubble)
        self.combat_group_sprite.remove(self.p1_turn_signal)
        self.combat_group_sprite.remove(self.p1_banner_1)
        self.combat_group_sprite.remove(self.p2_banner_2)
        self.combat_group_sprite.remove(self.p2_banner_1)
        self.combat_group_sprite.remove(self.p1_banner_2)

        self.combat_group_sprite.add(self.p2_end_sentence_button)
        self.combat_group_sprite.add(self.p2_dialogue_bubble)
        self.combat_group_sprite.add(self.p2_turn_signal)
