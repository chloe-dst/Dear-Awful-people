import pygame
import random
from mots import Mot

#paramètres pygame
WIDTH = 1080
HEIGHT = 720
FPS = 60
displaysurface = pygame.display.set_mode((WIDTH,HEIGHT))
step = 0

#choix personnage
Player1 = "not_defined"
Player2 = "not_defined"

#images fonds 
background1 = pygame.image.load('assets/illustration_menu.png')
background2 = pygame.image.load('assets/illustration_consignes.png')
background3 = pygame.image.load('assets/illustration_choixperso1.png')
background4 = pygame.image.load('assets/illustration_choixperso2.png')
background5 = pygame.image.load('assets/illustration_cartelieux.png')
background_bibliotheque = pygame.image.load('assets/illustration_biblio.png')
background_entree = pygame.image.load('assets/illustration_entree.png')
background_jardin = pygame.image.load('assets/illustration_jardin.png')
background_salleamanger = pygame.image.load('assets/illustration_salleamanger.png')
background_petitsalon = pygame.image.load('assets/illustration_petitsalon.png')

#images boutons
button1 = pygame.image.load('assets/illustration_menu-button.png')
button1 = pygame.transform.scale(button1, (300,100))
button2 = pygame.image.load('assets/illustration_consignes-button.png')
button2 = pygame.transform.scale(button2, (250,90))
buttonbiblio = pygame.image.load('assets/cartelieux_button_bibliotheque.png')
buttonsalon = pygame.image.load('assets/cartelieux_button_petitsalon.png')
buttonentree = pygame.image.load('assets/cartelieux_button_entree.png')
buttonjardin_locked = pygame.image.load('assets/cartelieux_button_jardin-locked.png')
buttonsalleamanger_locked = pygame.image.load('assets/cartelieux_button_salleamanger-locked.png')
buttonjardin_unlocked = pygame.image.load('assets/cartelieux_button_jardin-unlocked.png')
buttonsalleamanger_unlocked = pygame.image.load('assets/cartelieux_button_salleamanger-unlocked.png')
choixperso1 = pygame.image.load('assets/illustration_choixperso-perso1.png')
choixperso2 = pygame.image.load('assets/illustration_choixperso-perso2.png')
choixperso3 = pygame.image.load('assets/illustration_choixperso-perso3.png')
choixperso4 = pygame.image.load('assets/illustration_choixperso-perso4.png')
retourmenu = pygame.image.load('assets/button_retour-menu.png')

#combat
swearing_letter = pygame.image.load('assets/swearing_letter.png')
p1_end_sentence_button = pygame.image.load('assets/end_sentence_button.png')
p2_end_sentence_button = pygame.image.load('assets/end_sentence_button.png')
p1_dialogue_bubble = pygame.image.load('assets/bubble_dialogue_left.png')
p2_dialogue_bubble = pygame.image.load('assets/bubble_dialogue_right.png')
p1_turn_signal = pygame.image.load('assets/your_turn_signal_left.png')
p2_turn_signal = pygame.image.load('assets/your_turn_signal_right.png')
p1_banner_1 = pygame.image.load('assets/malus_1.png')
p2_banner_1 = pygame.image.load('assets/malus_1.png')
p1_banner_2 = pygame.image.load('assets/malus_2.png')
p2_banner_2 = pygame.image.load('assets/malus_2.png')

#images personnages
perso1_p1 = pygame.image.load('assets/perso1_p1.png')
perso2_p1 = pygame.image.load('assets/perso2_p1.png')
perso3_p1 = pygame.image.load('assets/perso3_p1.png')
perso4_p1 = pygame.image.load('assets/perso4_p1.png')
perso1_p2 = pygame.image.load('assets/perso1_p2.png')
perso2_p2 = pygame.image.load('assets/perso2_p2.png')
perso3_p2 = pygame.image.load('assets/perso3_p2.png')
perso4_p2 = pygame.image.load('assets/perso4_p2.png')

#liste des mots utilisables dans le combat
list_mots = [Mot("pauvre","adjectif","argent"), Mot("binoclard","adjectif","yeux"), Mot("laide","adjectif","épouse"),
             Mot("facheuse","adjectif","mère"), Mot("sénile","adjectif","age"), Mot("lilliputien","adjectif","taille"),
             Mot("besogneux","adjectif","argent"), Mot("aveugle","adjectif","yeux"), Mot("pouilleux","adjectif","argent"),
             Mot("stupide","adjectif","intelligence"), Mot("idiot","adjectif","intelligence"), Mot("pitoyable","adjectif","personnalité"),
             Mot("séduisante","adjectif","épouse"),
             #Nom
             Mot("votre strabisme","nom","yeux"), Mot("un dentier","nom","age"), Mot("des caries","nom","dent"),
             Mot("votre misérable mère","nom","mère"), Mot("personne","nom","célibataire"), Mot("paire de lunettes","nom","yeux"),
             Mot("la fête","nom","neutre"), Mot("hygiène","nom","odeur"), Mot("votre conjointe","nom","épouse"),
             Mot("votre bouche","nom", "dent"), Mot("petite vertue","nom","épouse"), Mot("dentifrice","nom", "odeur"),
             Mot("cocu", "nom", "épouse"), Mot("la jeune femme","nom","épouse"), Mot("votre face","nom","argent"),
             Mot("mon pauvre", "adjectif", "argent"),
             #Expression
             Mot("telle mère telle fille","expression","mère"), Mot("on sait tous que","expression","neutre"), Mot("pour votre enterrement", "expression","age"),
             Mot("rendre l'âme", "expression","age"),
             #Verbe
             Mot("cesser","verbe","neutre"), Mot("veuillez","verbe","neutre"), Mot("vous avez besoin de","verbe","neutre"),
             Mot("laisser moi rire de","verbe","neutre"), Mot("Vous avez","verbe","neutre"), Mot("j'ai","verbe","neutre"),
             Mot("vous êtes","verbe","neutre"), Mot("je suis","verbe","neutre"), Mot("ne vous aime","verbe","neutre"),
             Mot("il faut","verbe","neutre"), Mot("faîte attention","verbe","neutre"), Mot("vous manquez","verbe","neutre"),
             Mot("laisser","verbe","neutre"), Mot("cela ressemble à","verbe","neutre"), Mot("penser","verbe","neutre"),
             Mot("vous confondez","verbe","neutre"),
             #Autre
             Mot("pour", "autre", "neutre"), Mot("pour me", "autre", "neutre"),
             Mot("avec", "autre", "neutre"), Mot("comme", "autre", "neutre"), Mot("déjà", "autre", "neutre"),
             Mot("est une", "autre", "neutre"), Mot("est un", "autre", "neutre"), Mot("à votre", "autre", "neutre"),
             Mot("bientôt", "autre", "neutre"), Mot("dans", "autre", "neutre"), Mot("comme", "autre", "neutre"),
             Mot("il y a 20 ans", "autre", "age"), Mot("besoin de", "autre", "neutre"), Mot("ne pas s'étonner", "autre", "neutre"),
             Mot("vôtre", "autre", "neutre"),
             ]

list_mots_soutenu = [Mot("cuistre","adjectif","intelligence"), Mot("philistin","adjectif","intelligence"),
                     Mot("raclure de bidet","adjectif","odeur"), Mot("sagouin","adjectif","odeur"),
                     Mot("gourgandine","adjectif","épouse"), Mot("gaupe","adjectif","épouse"),
                     Mot("alvéopyge","adjectif","personnalité"), Mot("gougnafier","adjectif","célibataire"),
                     Mot("Hyperthyrroïdien des Alpes","adjectif","intelligence"), Mot("orchidoclaste","adjectif","personnalité"),
                     Mot("Foutriquet","adjectif","taille"), Mot("suprapygoflatulent","adjectif","intelligence"),
                     Mot("sulbaterne","adjectif","célibataire"), Mot("cossard","adjectif","célibataire"),
                     Mot("bélître","adjectif","argent"), Mot("pignouf","adjectif","personnalité"),
                     Mot("croquefredouille","adjectif","personnalité"),Mot("pestinentielle","adjectif","odeur"),
                     #Nom
                     Mot("indigence","nom","intelligence"),
                     Mot("esgourde","nom","oreille"), Mot("remugle","nom","odeur"),
                     Mot("myrmidon","nom","célibataire"), Mot("larbin","nom","épouse"),
                     Mot("ineptie","nom","intelligence"), Mot("imbroglio","nom","célibataire"),
                     #Expression
                     Mot("Je vous conchie","expression","intelligence"),Mot("on sait tous","expression","neutre"),
                     #Verbe
                     Mot("lanterner", "verbe", "célibataire")]

mots_affiches = []
list_mots_tous = list_mots + list_mots_soutenu