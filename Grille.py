dic = {'X' : 1, " " : 0, "U" : 2}


def lireGrille(chemin):
    fichier = open(chemin, "r")
    tmp = fichier.read()
    grille = []
    l = 0
    tmp = tmp.split('\n')
    for l in tmp:
        lig = []
        for c in l:
            lig.append(dic[c])
        grille.append(lig)
    return grille

