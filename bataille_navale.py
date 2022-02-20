# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:59:47 2019

@author: pauli
"""

# importation du module graphique 2D pygame
import pygame

# importation du module random
import random

# importation du module couleur et graphics
from couleur import *
from graphics import *


# Paramètres de la taille du jeu
N = 10
CASE = 50
WIDTH = N*CASE
HEIGHT = N*CASE
SIZE = [WIDTH, HEIGHT]

# Variables globales
jeu_soi = []
jeu_adv = []
bateau_pv_soi = []
bateau_pv_adv = []
bateau_id = []
coup_soi = []
coup_adv = []

#définition de constantes
VIDE = 0
TROUVE = 10
RATE = -1

#☺Couleur variable
COULEUR_GRILLE = blanc


""" --------------------------------------------------------------------------- 
    Partie 1 - AFFICHAGE DU QUADRILLAGE
--------------------------------------------------------------------------- """ 
    

def dessine_line_V(couleur):
    debut = [0, 0]
    fin = [0, HEIGHT]
    i = 0
    while i <= N :
        pygame.draw.line(screen, couleur, debut, fin, 1)
        pygame.display.flip()
        debut[0] = debut[0] + CASE
        fin[0] = fin[0] + CASE
        i = i + 1
        
        
def dessine_line_H(couleur):
    debut = [0, 0]
    fin = [WIDTH, 0]
    i = 0
    while i <= N :
        pygame.draw.line(screen, couleur, debut, fin, 1)
        pygame.display.flip()
        debut[1] = debut[1] + CASE
        fin[1] = fin[1] + CASE
        i = i + 1
        
        
def dessine_quadrillage(couleur):
    dessine_line_H(COULEUR_GRILLE)
    dessine_line_V(COULEUR_GRILLE)


""" --------------------------------------------------------------------------- 
    Partie 2 - INITIALISATION DU TABLEAU
--------------------------------------------------------------------------- """    


#initialiser le tableau de jeu avec des cases non jouées = 0    

def init_jeu_soi():
    i = 0
    while i < N :
        # ajout d'une ligne i dans le tableau jeu
        jeu_soi.append([])
        j = 0
        while j < N :
            # ajout d'une colonne j contenant un 0 dans la ligne i
            jeu_soi[i].append(VIDE)
            j = j + 1
        i = i + 1


def init_coup_soi():
    i = 0
    while i < N :
        # ajout d'une ligne i dans le tableau jeu
        coup_soi.append([])
        j = 0
        while j < N :
            # ajout d'une colonne j contenant un 0 dans la ligne i
            coup_soi[i].append(VIDE)
            j = j + 1
        i = i + 1
        
def affiche_jeu_console_soi():
    print("jeu :")
    # parcours des lignes du tableau jeu
    i = 0
    while i<N:
        # parcours des colonnes du tableau jeu
        j = 0
        while j<N:
            print('{:>2}'.format(jeu_soi[i][j]), end=" ")
            j +=1
        print("\n")
        i +=1

def affiche_coup_soi():
    print("jeu :")
    # parcours des lignes du tableau jeu
    i = 0
    while i<N:
        # parcours des colonnes du tableau jeu
        j = 0
        while j<N:
            print('{:>2}'.format(coup_soi[i][j]), end=" ")
            j +=1
        print("\n")
        i +=1
        
def init_jeu_adv():
    i = 0
    while i < N :
        # ajout d'une ligne i dans le tableau jeu
        jeu_adv.append([])
        j = 0
        while j < N :
            # ajout d'une colonne j contenant un 0 dans la ligne i
            jeu_adv[i].append(VIDE)
            j = j + 1
        i = i + 1
 
    
def init_coup_adv():
    i = 0
    while i < N :
        # ajout d'une ligne i dans le tableau jeu
        coup_adv.append([])
        j = 0
        while j < N :
            # ajout d'une colonne j contenant un 0 dans la ligne i
            coup_adv[i].append(VIDE)
            j = j + 1
        i = i + 1

        
def affiche_jeu_console_adv():
    print("jeu :")
    # parcours des lignes du tableau jeu
    i = 0
    while i<N:
        # parcours des colonnes du tableau jeu
        j = 0
        while j<N:
            print('{:>2}'.format(jeu_adv[i][j]), end=" ")
            j +=1
        print("\n")
        i +=1
  
def affiche_coup_adv():
    print("jeu :")
    # parcours des lignes du tableau jeu
    i = 0
    while i<N:
        # parcours des colonnes du tableau jeu
        j = 0
        while j<N:
            print('{:>2}'.format(coup_adv[i][j]), end=" ")
            j +=1
        print("\n")
        i +=1    
    
#initiliser les 5 bateaux à un identifiant qui permet de le repérer plus facilement
def init_bateau_id():
    bateau_id.append(1)
    bateau_id.append(2)
    bateau_id.append(3)
    bateau_id.append(4)
    bateau_id.append(5)


def affiche_bateau_id_console():
    print("id :")
    i = 0
    while i<5 :
        print(bateau_id[i])
        i+=1


#initialiser les points de pv de chaque bateaux pour savoir à quel moment il sera coulé   
def init_bateau_pv():
    bateau_pv_soi.append(2)
    bateau_pv_soi.append(3)
    bateau_pv_soi.append(3)
    bateau_pv_soi.append(4)
    bateau_pv_soi.append(5)
    bateau_pv_adv.append(2)
    bateau_pv_adv.append(3)
    bateau_pv_adv.append(3)
    bateau_pv_adv.append(4)
    bateau_pv_adv.append(5)

    
def affiche_bateau_pv_console():
    print("pv :")
    i = 0
    while i<5 :
        print(bateau_pv_soi[i], bateau_pv_adv[i])
        i+=1


""" --------------------------------------------------------------------------- 
    Partie 3 - Validité de la saisie
--------------------------------------------------------------------------- """


def bateau(couleur,rect):
    pygame.draw.rect(screen, couleur, rect, 0)
    pygame.display.flip()
    
   
def position_possible(i1, j1, pv, id, couleur):
    print("i1 =",i1,", j1 =",j1)
    # variables pour déterminer la validité des saisies dans les 4 directions
    valide_bas = 1
    valide_haut = 1
    valide_droite = 1
    valide_gauche = 1
    # 1) affichage de l'aide à la saisie en bas
    # test du débordement du tableau en bas
    if i1 + pv - 1 >= N:
        valide_bas = 0
    else:
        # test des cases vides en bas
        i = 0
        while i < pv :
            # case non vide
            if jeu_soi[i1+i][j1] != 0:
                valide_bas = 0
            i = i + 1
        # la saisie en bas est possible
        if valide_bas == 1:
            l = CASE
            h = pv*CASE
            x = j1*CASE
            y = i1*CASE
            rect_bas = [x, y, l, h]
            bateau(couleur,rect_bas)
    # 2) affichage de l'aide à la saisie en haut
    if i1 - pv < -1:
        valide_haut = 0
    else:
        i = 0
        while i < pv :
            if jeu_soi[i1-i][j1] != 0:
                valide_haut = 0
            i = i + 1
        if valide_haut == 1 :
            l = CASE
            h = pv * CASE
            x = j1*CASE
            y = (i1-pv+1)*CASE
            rect_h = [x, y, l, h]
            bateau(couleur,rect_h)
    # 3) affichage de l'aide à la saisie à droite
    if j1 + pv - 1 >= N:    
        valide_droite = 0
    else:
        i = 0
        while i < pv :
            if jeu_soi[i1][j1+i] != 0:
                valide_droite = 0
            i = i + 1
        if valide_droite == 1 :
            l = pv * CASE
            h = CASE
            x = j1*CASE
            y = i1*CASE
            rect_d = [x, y, l, h]
            bateau(couleur,rect_d)
    # 1) affichage de l'aide à la saisie à gauche
    if j1 - pv <= -2 :
        valide_gauche = 0
    else:
        i = 0
        while i < pv :
            if jeu_soi[i1][j1-i] != 0:
                valide_gauche = 0
            i = i + 1
        if valide_gauche == 1 :
            l = pv*CASE
            h = CASE
            x = (j1-pv+1)*CASE
            y = i1*CASE
            rect_g = [x, y, l, h]
            bateau(couleur,rect_g)
    # si aucune direction n'est valide, la saisie n'est pas valide !
    print("valide_bas =", valide_bas)
    print("valide_haut =", valide_haut)
    print("valide_gauche =", valide_gauche)
    print("valide_droite =", valide_droite)
    if (valide_bas == 1 or
        valide_haut == 1 or
        valide_gauche == 1 or
        valide_droite == 1):
        valide = 1
    else:
        valide = 0
    print("valide =", valide)
    return valide


def position_possible_adv(i1, j1, pv, id):
    print("i1 =",i1,", j1 =",j1)
    # variables pour déterminer la validité des saisies dans les 4 directions
    valide_bas = 1
    valide_haut = 1
    valide_droite = 1
    valide_gauche = 1
    # test du débordement du tableau en bas
    if i1 + pv - 1 >= N:
        valide_bas = 0
    else:
        # test des cases vides en bas
        i = 0
        while i < pv :
            # case non vide
            if jeu_adv[i1+i][j1] != 0:
                valide_bas = 0
            i = i + 1
        # la saisie en bas est possible
    # test du débordement du tableau en haut
    if i1 - pv < -1:
        valide_haut = 0
    else:
        i = 0
        while i < pv :
            if jeu_adv[i1-i][j1] != 0:
                valide_haut = 0
            i = i + 1
    # test du débordement du tableau à droite
    if j1 + pv - 1 >= N:    
        valide_droite = 0
    else:
        i = 0
        while i < pv :
            if jeu_adv[i1][j1+i] != 0:
                valide_droite = 0
            i = i + 1
    # test du débordement du tableau à gauche
    if j1 - pv <= -2 :
        valide_gauche = 0
    else:
        i = 0
        while i < pv :
            if jeu_adv[i1][j1-i] != 0:
                valide_gauche = 0
            i = i + 1
    # si aucune direction n'est valide, la saisie n'est pas valide !
    print("valide_bas =", valide_bas)
    print("valide_haut =", valide_haut)
    print("valide_gauche =", valide_gauche)
    print("valide_droite =", valide_droite)
    if (valide_bas == 1 or
        valide_haut == 1 or
        valide_gauche == 1 or
        valide_droite == 1):
        valide = 1
    else:
        valide = 0
    print("valide =", valide)
    return valide


def valide_saisie(i1, j1, i2, j2, pv, id):
    print("i2 =", i2, ",j2 =", j2)
    # variables pour déterminer la validité des saisies dans les 4 directions
    valide_bas = 1
    valide_haut = 1
    valide_droite = 1
    valide_gauche = 1
    # 1) validité de la saisie en bas
    # Les deux clics doivent être dans la même colonne
    if j1 != j2:
        valide_bas = 0
    else :
        if i1 == i2:
            valide_bas = 0
        elif i1 + pv > 10:
            valide_bas = 0
        elif i2 - i1 > pv or i2 - i1 < 0:
            valide_bas = 0
        else :
            # il ne doit y avoir que des cases vides entre i1 et i2
            i = 0
            while i < pv:
                if jeu_soi[i1+i][j1] != 0:
                        valide_bas = 0
                i+=1
            # la saisie est valide, on met à jour le tableau jeu
            if valide_bas == 1:
                i = 0
                while i < pv:
                    jeu_soi[i1+i][j1] = id
                    i+=1
    # 2) validité de la saisie en haut
    if j1 != j2:
        valide_haut = 0
    else :
        if i1 == i2 :
            valide_haut = 0
        elif i1 - pv < -1 :
            valide_haut = 0
        elif i1 - i2 > pv or i1 - i2 < 0:
            valide_haut = 0
        else :
            i = 0
            while i < pv:
                if jeu_soi[i1-i][j1] != 0:
                        valide_haut = 0
                i = i + 1
            if valide_haut == 1:
                i = 0
                while i < pv:
                    jeu_soi[i1-i][j1] = id
                    i = i + 1
    # 3) validité de la saisie à gauche
    if i1 != i2:
        valide_gauche = 0
    else :
        if j1 == j2:
            valide_gauche = 0
        elif j1 - pv < -1:
            valide_gauche = 0
        elif j1 - j2 > pv or j1 - j2 < 0:
            valide_gauche = 0
        else :
            i = 0
            while i < pv:
                if jeu_soi[i1][j1-i] != 0:
                        valide_gauche = 0
                i = i + 1
            if valide_gauche == 1:
                i = 0
                while i < pv:
                    jeu_soi[i1][j1-i] = id
                    i = i + 1
    # 4) validité de la saisie à droite
    if i1 != i2:
        valide_droite = 0
    else :
        if j1 == j2:
            valide_droite = 0
        elif j1 + pv > 10:
            valide_droite = 0
        elif j2 - j1 > pv or j2 - j1 < 0:
            valide_droite = 0
        else :
            i = 0
            while i < pv:
                if jeu_soi[i1][j1+i] != 0:
                        valide_droite = 0
                i = i + 1
            if valide_droite == 1:
                i = 0
                while i < pv:
                    jeu_soi[i1][j1+i] = id
                    i = i + 1
    print("valide_bas =", valide_bas)
    print("valide_haut =", valide_haut)
    print("valide_gauche =", valide_gauche)
    print("valide_droite =", valide_droite)
    print( i1, j1)
    # Si aucune direction n'est valide, la saisie n'est pas valide
    if ((valide_bas == 1) or
        (valide_haut == 1) or
        (valide_gauche == 1) or
        (valide_droite == 1)):
        valide = 1
    else:
        valide = 0
    print("valide =", valide)
    return valide
         
       
def valide_saisie_adv(i1, j1, i2, j2, pv, id):
    print("i2 =", i2, ",j2 =", j2)
    valide_bas = 1
    valide_haut = 1
    valide_droite = 1
    valide_gauche = 1
    # 1) validité de la saisie en bas
    if j1 != j2:
        valide_bas = 0
    else :
        if i1 == i2:
            valide_bas = 0
        elif i1 + pv > 10:
            valide_bas = 0
        elif i2 - i1 > pv or i2 - i1 < 0:
            valide_bas = 0
        else :
            i = 0
            while i < pv:
                if jeu_adv[i1+i][j1] != 0:
                        valide_bas = 0
                i+=1
            if valide_bas == 1:
                i = 0
                while i < pv:
                    jeu_adv[i1+i][j1] = id
                    i+=1
    # 2) validité de la saisie en haut
    if j1 != j2:
        valide_haut = 0
    else :
        if i1 == i2 :
            valide_haut = 0
        elif i1 - pv < -1 :
            valide_haut = 0
        elif i1 - i2 > pv or i1 - i2 < 0:
            valide_haut = 0
        else :
            i = 0
            while i < pv:
                if jeu_adv[i1-i][j1] != 0:
                        valide_haut = 0
                i = i + 1
            if valide_haut == 1:
                i = 0
                while i < pv:
                    jeu_adv[i1-i][j1] = id
                    i = i + 1
    # 3) validité de la saisie à gauche
    if i1 != i2:
        valide_gauche = 0
    else :
        if j1 == j2:
            valide_gauche = 0
        elif j1 - pv < -1:
            valide_gauche = 0
        elif j1 - j2 > pv or j1 - j2 < 0:
            valide_gauche = 0
        else :
            i = 0
            while i < pv:
                if jeu_adv[i1][j1-i] != 0:
                        valide_gauche = 0
                i = i + 1
            if valide_gauche == 1:
                i = 0
                while i < pv:
                    jeu_adv[i1][j1-i] = id
                    i = i + 1
    # 4) validité de la saisie à droite
    if i1 != i2:
        valide_droite = 0
    else :
        if j1 == j2:
            valide_droite = 0
        elif j1 + pv > 10:
            valide_droite = 0
        elif j2 - j1 > pv or j2 - j1 < 0:
            valide_droite = 0
        else :
            i = 0
            while i < pv:
                if jeu_adv[i1][j1+i] != 0:
                        valide_droite = 0
                i = i + 1
            if valide_droite == 1:
                i = 0
                while i < pv:
                    jeu_adv[i1][j1+i] = id
                    i = i + 1
    print("valide_bas =", valide_bas)
    print("valide_haut =", valide_haut)
    print("valide_gauche =", valide_gauche)
    print("valide_droite =", valide_droite)
    print( i1, j1)
    if ((valide_bas == 1) or
        (valide_haut == 1) or
        (valide_gauche == 1) or
        (valide_droite == 1)):
        valide = 1
    else:
        valide = 0
    print("valide =", valide)
    return valide


""" --------------------------------------------------------------------------- 
    Partie 4 - Saisie des bateaux
--------------------------------------------------------------------------- """


def saisie_bateau_soi(pv,id):
    clic1 = wait_clic()
    i1 = clic1[1]//CASE
    j1 = clic1[0]//CASE
    while position_possible(i1, j1, pv, id, gris) != 1:
        clic1 = wait_clic()
        i1 = clic1[1]//CASE
        j1 = clic1[0]//CASE
        while jeu_soi[i1][j1] != 0 :
            clic1 = wait_clic()
            i1 = clic1[1]//CASE
            j1 = clic1[0]//CASE
    clic2 = wait_clic()
    i2 = clic2[1]//CASE
    j2 = clic2[0]//CASE
    while i1 == i2 and j1 == j2:
        clic2 = wait_clic()
        i2 = clic2[1]//CASE
        j2 = clic2[0]//CASE

    while valide_saisie(i1, j1, i2, j2, pv, id) != 1:
        clic2 = wait_clic()
        i2 = clic2[1]//CASE
        j2 = clic2[0]//CASE
    if i1 == i2 :
        if j2 - j1 > 0:
            l = pv*CASE
            h = CASE
            x = j1*CASE
            y = i1*CASE
        elif j2 - j1 < 0:
            l = pv*CASE
            h = CASE
            x = (j1-pv+1)*CASE
            y = i1*CASE
    elif j1 == j2 :
        if i2 - i1 > 0:
            l = CASE
            h = pv*CASE
            x = j1*CASE
            y = i1*CASE
        else :
            l = CASE
            h = pv*CASE
            x = j1*CASE
            y = (i1-pv+1)*CASE
    rect_f = [x, y, l, h]
    bateau(bleu,rect_f)
    affiche_jeu_console_soi()


def saisie_bateau_adv(pv,id):
    i1 = random.randint(0,HEIGHT)//CASE
    j1 = random.randint(0,HEIGHT)//CASE
    while position_possible_adv(i1, j1, pv, id) != 1:
        i1 = random.randint(0,HEIGHT)//CASE
        j1 = random.randint(0,HEIGHT)//CASE
        while jeu_adv[i1][j1] != 0 :
            i1 = random.randint(0,HEIGHT)//CASE
            j1 = random.randint(0,HEIGHT)//CASE
    i2 = random.randint(0,HEIGHT)//CASE
    j2 = random.randint(0,HEIGHT)//CASE
    while i1 == i2 and j1 == j2:
        i2 = random.randint(0,HEIGHT)//CASE
        j2 = random.randint(0,HEIGHT)//CASE
    while valide_saisie_adv(i1, j1, i2, j2, pv, id) != 1:
        i2 = random.randint(0,HEIGHT)//CASE
        j2 = random.randint(0,HEIGHT)//CASE
    affiche_jeu_console_adv()


""" --------------------------------------------------------------------------- 
    Partie 5 - Initialisation des coups
--------------------------------------------------------------------------- """

def attaque_soi() :
    clic1 = wait_clic()
    i1 = clic1[1]//CASE
    j1 = clic1[0]//CASE
    while coup_soi[i1][j1] != 0:
        clic1 = wait_clic()
        i1 = clic1[1]//CASE
        j1 = clic1[0]//CASE
    if jeu_adv[i1][j1] == 0:
        coup_soi[i1][j1] = -1
    if jeu_adv[i1][j1] > 0:
        if jeu_adv[i1][j1] == 5:
            bateau_pv_adv[5-1] = bateau_pv_adv[5-1] - 1
        if jeu_adv[i1][j1] == 4:
            bateau_pv_adv[4-1] = bateau_pv_adv[4-1] - 1
        if jeu_adv[i1][j1] == 3:
            bateau_pv_adv[3-1] = bateau_pv_adv[3-1] - 1
        if jeu_adv[i1][j1] == 2:
            bateau_pv_adv[2-1] = bateau_pv_adv[2-1] - 1
        if jeu_adv[i1][j1] == 1:
            bateau_pv_adv[1-1] = bateau_pv_adv[1-1] - 1
        coup_soi[i1][j1] = 1
    affiche_bateau_pv_console()


def attaque_adv() :
    i1 = random.randint(0,HEIGHT)//CASE
    j1 = random.randint(0,WIDTH)//CASE
    while i1 >= 10 or j1 >= 10:
        i1 = random.randint(0,HEIGHT)//CASE
        j1 = random.randint(0,WIDTH)//CASE
        while coup_adv[i1][j1] != 0:
            i1 = random.randint(0,HEIGHT)//CASE
            j1 = random.randint(0,WIDTH)//CASE
    if jeu_soi[i1][j1] == 0:
        coup_adv[i1][j1] = -1
    if jeu_soi[i1][j1] > 0:
        if jeu_soi[i1][j1] == 5:
            bateau_pv_soi[5-1] = bateau_pv_soi[5-1] - 1
        if jeu_soi[i1][j1] == 4:
            bateau_pv_soi[4-1] = bateau_pv_soi[4-1] - 1
        if jeu_soi[i1][j1] == 3:
            bateau_pv_soi[3-1] = bateau_pv_soi[3-1] - 1
        if jeu_soi[i1][j1] == 2:
            bateau_pv_soi[2-1] = bateau_pv_soi[2-1] - 1
        if jeu_soi[i1][j1] == 1:
            bateau_pv_soi[1-1] = bateau_pv_soi[1-1] - 1
        coup_adv[i1][j1] = 1
    affiche_bateau_pv_console()


""" --------------------------------------------------------------------------- 
    Partie 6 - Mise en place du jeu
--------------------------------------------------------------------------- """


def affiche_jeu(joueur):
    pygame.draw.rect(screen, noir, [0, 0, WIDTH,HEIGHT], 0)
    print("joueur =",joueur)
    i = 0
    while i < N :
        # ajout d'une ligne i dans le tableau jeu
        j = 0
        while j < N :
            # ajout d'une colonne j contenant un 0 dans la ligne i
            rect = [j*CASE, i*CASE, CASE, CASE]
            if joueur == 1:
                if coup_soi[i][j] == -1:
                    pygame.draw.rect(screen, gris, rect, 0)
                elif coup_soi[i][j] > 0:
                    pygame.draw.rect(screen, rouge, rect, 0)
            elif joueur == -1:
                if jeu_soi[i][j] > 0:
                    pygame.draw.rect(screen, bleu, rect, 0)
                if coup_adv[i][j] == -1:
                    pygame.draw.rect(screen, gris, rect, 0)
                elif coup_adv[i][j] > 0:
                    pygame.draw.rect(screen, rouge, rect, 0)
            j = j + 1
        i = i + 1
    dessine_quadrillage(blanc)


""" --------------------------------------------------------------------------- 
    Partie 6 - programme principal
--------------------------------------------------------------------------- """


# initialisation du module d'affichage 2D pygame
pygame.display.init()


# Création et affichage de la fenêtre graphique de largeur 900 et hauteur 600
size = [WIDTH, HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.flip()


# Initialisation du jeu
init_jeu_soi()
init_coup_soi()
init_jeu_adv()
init_coup_adv()
init_bateau_id()
init_bateau_pv()
affiche_jeu_console_soi()


# Dessin du quadrillage
dessine_quadrillage(COULEUR_GRILLE)


# Saisie des bateaux pour soi
joueur = -1
i = 0
while i < 5:
    saisie_bateau_soi(bateau_pv_soi[i], bateau_id[i])
    affiche_jeu(joueur)
    i = i + 1
affiche_jeu_console_soi()


# Saisie des bateaux de l'adversaire
i = 0
while i < 5:
    saisie_bateau_adv(bateau_pv_adv[i], bateau_id[i])
    i = i + 1
affiche_jeu_console_adv()    
    

# jeu
joueur = 1
encore = 1
while encore != 0:
    # affiche du jeu selon le joeur    
    affiche_jeu(joueur)
    if joueur == 1 :    
        affiche_jeu_console_soi()
        attaque_soi()
        affiche_coup_soi()
    else :
        affiche_jeu_console_adv()
        attaque_adv()
        affiche_coup_adv()
    affiche_jeu(joueur)
    clic = wait_clic()
    
    # test gagnant
    if joueur == 1:
        i = 0
        coulé = 0
        while i < 5:
            if bateau_pv_adv[i] == 0:  
                coulé = coulé + 1
            i = i + 1
        if coulé == 5:
            print("le joueur ", joueur, " a gagné !")
            encore = encore - 1
    elif joueur == -1:
        i = 0
        coulé = 0
        while i < 5:
            if bateau_pv_soi[i] == 0:
                coulé = coulé + 1
            i = i + 1
        if coulé == 5:
            print("le joueur ", joueur, " a gagné !")
            encore = encore - 1
    
    # changement de joueur
    joueur = -joueur

# sortie du programme
wait_escape()
pygame.quit()