class Labyrinthe:
    #attributs de la classe Labyrinthe
    nbLignes = 0
    nbCol = 0
    grille = [0][0]
    nbJoueurs = 0
    robots = []


    def __init__(self, grille, robots = []):
        self.grille = grille
        self.nbLignes = len(grille)
        self.nbCol = len(grille [0])
        self.robots = robots
        self.nbJoueurs = len(robots)

    @property
    def getNbLignes(self):
        return self.nbLignes
    @property
    def getNbCol(self):
        return self.nbCol
    @property
    def getGrille(self):
        return self.grille
    @property
    def getNbJoueurs(self):
        return self.nbJoueurs
    @property
    def getRobots(self):
        return self.robots

    @property
    def setGrille(self, gril):
        self.grille = gril
        self.nbLignes = len(gril)
        self.nbCol = len(gril[0])

    def __str__(self):
        rep = ""
        for ligne in self.grille:
            for colonne in ligne:
                if(self.estRobot(ligne, colonne)):
                    rep += self.getRobot(ligne, colonne).getSymb
                else:
                    rep += colonne
            rep += "\n"
        return rep

    def addRobot(self, rob):
        self.robots.append(rob)
        self.nbJoueurs += 1

    def estRobot(self, lig, col):
        for robot in self.robots:
            if(robot.getX == lig):
                if(robot.getY == col):
                    return True
        return False

    def getRobot(self, lig, col):
        for robot in self.robots:
            if(robot.getX() == lig and robot.getY() == col):
                return robot
        return False
