from data import *
from images import Image
from characters import Character
from combat import Combat
from launch import Launch
from mots import Mot
from math import floor
from random import randint

#lancement et paramètres pygame 
pygame.init()
frame_per_second = pygame.time.Clock()
pygame.display.set_caption("Dear awful people,")

menu = Launch()
fight = Combat()
mouse = pygame.mouse.get_pos()

#AJOUT JOEY
first = floor(randint(1,2)) #J'AI L'IMPRESSION QUE CE N'EST PAS UTILISE
i = 0

x = 100
y = 100 

while True:
    # affichage de l'écran de départ
    for entity in menu.backgrounds_sprites:
        displaysurface.blit(entity.image,entity.rect)
    for entity in menu.buttons_sprites:
        displaysurface.blit(entity.image,entity.rect)
    for entity in menu.combat_group_sprite:
        if fight.is_playing :
            displaysurface.blit(entity.image,entity.rect)
    
    #l'affichage des écrans se met à jour en fonction de la variable step qui augmente au clic sur les boutons
    if step == 1: 
        menu.backgrounds_sprites.remove(menu.Background1)
        menu.buttons_sprites.remove(menu.button_menu)
        menu.backgrounds_sprites.add(menu.Background2)
        menu.buttons_sprites.add(menu.button_consignes)
    if step == 2 :
        menu.backgrounds_sprites.remove(menu.Background2) 
        menu.buttons_sprites.remove(menu.button_consignes)
        menu.backgrounds_sprites.add(menu.Background3)
        menu.buttons_sprites.add(menu.choix_perso1)
        menu.buttons_sprites.add(menu.choix_perso2)
        menu.buttons_sprites.add(menu.choix_perso3)
        menu.buttons_sprites.add(menu.choix_perso4)
    if step == 3 : 
        menu.backgrounds_sprites.remove(menu.Background3)
        menu.backgrounds_sprites.add(menu.Background4)
    if step == 4 :
        menu.buttons_sprites.remove(menu.choix_perso1)
        menu.buttons_sprites.remove(menu.choix_perso2)
        menu.buttons_sprites.remove(menu.choix_perso3)
        menu.buttons_sprites.remove(menu.choix_perso4) 
        menu.backgrounds_sprites.remove(menu.Background4)
        menu.start(fight)

    #affiche et met à jour le nombre de parties jouées
    if step > 3 and fight.is_playing == False : 
        menu.parties_played(fight)

    #si le combat est en cours
    if fight.is_playing == True: 
        p1.update_scorebar(displaysurface)
        p2.update_scorebar(displaysurface)
        menu.combat_group_sprite.add(menu.swearing_letter)
        fight.afficher_mots_affiches()
        # affichage des phrases en fonction du tour des joueurs
        if p1.own_turn < p2.own_turn :
            fight.display_of_sentence_p1_playing(p1,2000, 205, 75, 920, 108,p2)
        else :
            fight.display_of_sentence_p2_playing(p2,2000, 150, 75, 852, 108,p1)

    if fight.winner == True: 
      fight.final_score(displaysurface, menu, p1, p2)

    #gestion des évènements    
    for event in pygame.event.get(): 
        key_pressed = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit() 
        
        elif event.type == pygame.MOUSEBUTTONUP:
            for entity in menu.buttons_sprites:
                if entity.rect.collidepoint(event.pos): 
                    step += 1
            if step == 3 :
                if menu.choix_perso1.rect.collidepoint(event.pos) :
                    Player1 = "1"
                    menu.buttons_sprites.remove(menu.choix_perso1)
                    p1 = Character("Norfolk", ["yeux", "épouse", "argent"], perso1_p1, 1)
                elif menu.choix_perso2.rect.collidepoint(event.pos) :
                    Player1 = "2"
                    menu.buttons_sprites.remove(menu.choix_perso2)
                    p1 = Character("Berkley", ["odeur", "oreille", "personnalité"], perso2_p1, 1)
                elif menu.choix_perso3.rect.collidepoint(event.pos) :
                    Player1 = "3"
                    menu.buttons_sprites.remove(menu.choix_perso3)
                    p1 = Character("Cordiff", ["taille", "intelligence", "mère"], perso3_p1, 1)
                elif menu.choix_perso4.rect.collidepoint(event.pos) :
                    Player1 = "4"
                    menu.buttons_sprites.remove(menu.choix_perso4)
                    p1 = Character("Surrey", ["dent", "célibataire", "age"], perso4_p1, 1)
            if step == 4 :
                if menu.choix_perso1.rect.collidepoint(event.pos) :
                    Player2 = "1"
                    menu.buttons_sprites.remove(menu.choix_perso1)
                    p2 = Character("Norfolk", ["yeux", "épouse", "argent"], perso1_p2, 2)
                elif menu.choix_perso2.rect.collidepoint(event.pos) :
                    Player2 = "2"
                    p2 = Character("Berkley", ["odeur", "oreille", "personnalité"], perso2_p2, 2)
                elif menu.choix_perso3.rect.collidepoint(event.pos) :
                    Player2 = "3"
                    p2 = Character("Cordiff", ["taille", "intelligence", "mère"], perso3_p2, 2)
                elif menu.choix_perso4.rect.collidepoint(event.pos) :
                    Player2 = "4"
                    p2 = Character("Surrey", ["dent", "célibataire", "age"], perso4_p2, 2)
            if step > 4 and fight.is_playing == False : 
            #zones cliquables seulement dans le menu
                if menu.button_bibliotheque.rect.collidepoint(event.pos) :
                    fight.level = "bibliotheque"
                    menu.end(fight,displaysurface,menu,p1,p2)
                    menu.backgrounds_sprites.add(menu.Background_bibliotheque)
                if menu.button_entree.rect.collidepoint(event.pos) :
                    fight.level = "entree" 
                    menu.end(fight,displaysurface,menu,p1,p2)
                    menu.backgrounds_sprites.add(menu.Background_entree)
                if menu.button_petitsalon.rect.collidepoint(event.pos) :
                    fight.level = "petit salon" 
                    menu.end(fight,displaysurface,menu,p1,p2)
                    menu.backgrounds_sprites.add(menu.Background_petitsalon)
                if menu.button_jardin_unlocked.rect.collidepoint(event.pos) and fight.level_jardin == True  : 
                    fight.level = "jardin"
                    menu.end(fight,displaysurface,menu,p1,p2)
                    menu.backgrounds_sprites.add(menu.Background_jardin)
                if menu.button_salleamanger_unlocked.rect.collidepoint(event.pos) and fight.level_salleamanger == True : 
                    fight.level = "salle a manger"
                    menu.end(fight,displaysurface,menu,p1,p2)
                    menu.backgrounds_sprites.add(menu.Background_salleamanger)
            if step > 4 and fight.is_playing == True : 
                #zones cliquable seulement pendant le combat
                pygame.time.wait(200)

                if fight.first_turn == 0 :
                    fight.first_player_choice(p1, p2, menu)
                else :
                    if p1.own_turn < p2.own_turn :
                        menu.visibility_object_fight_p1()
                        if pygame.mouse.get_pressed() :
                            fight.click_word(p1,menu,p1,p2)
                            p1.own_turn += 2
                    else:
                        menu.visibility_object_fight_p2()
                        if pygame.mouse.get_pressed() :
                            fight.click_word(p2,menu,p1,p2)
                            p2.own_turn += 2
                
                if fight.winner == False :
                    #clic pour arrêter l'ajout de mots à la liste 
                    if len(mots_affiches) - 1 == 0 :
                        fight.both_end_sentence(p1, p2)
                    if menu.p1_end_sentence_button.rect.collidepoint(event.pos) and p2.end_sentence == True :
                        p1.end_sentence = True
                        fight.both_end_sentence(p1,p2)
                    if menu.p2_end_sentence_button.rect.collidepoint(event.pos) and p1.end_sentence == True :
                        p2.end_sentence = True
                        fight.both_end_sentence(p1, p2)
                    if menu.p2_end_sentence_button.rect.collidepoint(event.pos) and p1.end_sentence == False :
                        p2.end_sentence = True
                        menu.visibility_object_fight_p1()
                    if menu.p1_end_sentence_button.rect.collidepoint(event.pos) and p2.end_sentence == False :
                        p1.end_sentence = True
                        menu.visibility_object_fight_p2()

                if menu.button_retourmenu.rect.collidepoint(event.pos) and fight.winner == True:
                    #fin du combat, reset personnages et retour au menu 
                    menu.combat_group_sprite.remove(menu.button_retourmenu)
                    p1.end_sentence = False
                    p2.end_sentence = False
                    p1.my_awful_sentence = []
                    p2.my_awful_sentence = []
                    p1.own_turn = 0
                    p2.own_turn = 0
                    fight.first_turn = 0
                    fight.winner = False
                    fight.end(menu,p1,p2)
                    menu.start(fight)
                
    #mise à jour du jeu
    pygame.display.flip()
    frame_per_second.tick(FPS)