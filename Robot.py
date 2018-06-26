class Robot:
    #attributs de la classe Robot : Coordonnees x et y ainsi que le nb de coups joues
    x = 0
    y = 0
    nbCoups = 0

    def __init__(self, x, y, nb = 0):
        #initialise le robot a x et y avec eventuellement nb coups deja portes
        self.x = x
        self.y = y
        self.nbCoups = nb

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getNb(self):
        return self.nbCoups



    def __setattr__(self, key, value):
        self.key = value



    def __str__(self):
        #Representation de Robot en chaine de caracteres : Coordonnees et nb de coups joues (mode devt)
        return ("Robot : " + self.x + " , " + self.y + " : " + self.nbCoups + " coups joues.")


    def deplacement(self, direction):
        """ Direction : char parmi 'N' = Nord, 'S' = Sud, 'O' = Ouest, 'E' = Est
        Deplace le robot vers direction, retourne un booleen correspondant a la reussite de l'appel"""
        if  direction == 'N':
            self.x -= 1
            self.nbCoups += 1
            return True
        elif direction == 'S':
            self.x += 1
            self.nbCoups += 1
            return True
        elif direction == 'O':
            self.y -= 1
            self.nbCoups += 1
            return True
        elif direction == 'S':
            self.y += 1
            self.nbCoups += 1
            return True
        else:
            return False



    def murer(direction):
        return True

    def percer(direction):
        return True
