from os import *

dic = {'X' : 1, " " : 0, "U" : 2}

def ouvrirFichier(chemin):
    fichier = fopen(chemin)
    grille = []


def listeGrille(dossier = "/"):
    rep =[]
    fichiers = listdir(dossier)
    for f in fichiers:
        rep.append(f.split('.')[0])
    return rep

def affListeGrilles():
    l = listeGrille()
    for g in l:
        print(g + " ;")
