class Labyrinthe:
    #attributs de la classe Labyrinthe
    nbLignes = 0
    nbCol = 0
    grille = [][]
    nbJoueurs = 0
    robots = []


    def __init__(self, grille, robots):
        self.grille = grille
        self.nbLignes = len(grille)
        self.nbCol = len(grille [0])
        self.robots = robots
        self.nbJoueurs = len(robots)


    def __str__(self):
        rep = ""
        for ligne in self.grille:
            for colonne in ligne:
                if(estRobot(ligne, colonne)):
                    rep += 'R'
                else:
                    rep += colonne
            rep += "\n"
        return rep

    def estRobot(self, lig, col):
        for robot in self.robots:
            if(robot.getX == lig):
                if(robot.getY == col):
                    return True
        return False

    



