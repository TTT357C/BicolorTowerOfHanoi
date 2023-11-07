"""
classe che rappresenta un generico stato del gioco.
    - Memorizza l'elenco di rod
    - definisce un metodo per il cofronto tra due stati
    - definisce un metodo che dato uno stato ritorna le azioni possibili
"""
import numpy as np
from State_C1 import heutristicCalc, aP_C

class State:

    def __init__(self, rods, g) -> None:
        self.rods = rods
        self.g = g


    def __eq__(self, other) -> bool:
        return all(self.rods[i] == other.rods[i] for i in range(len(self.rods)))

    def __hash__(self):
        return hash(self.toString_())
    
    def toString_(self):
        s = "\n"
        for i, r in enumerate(self.rods, start=1):
            s += f"paletto {str(i)}\n{r.toString()}\n"
        s += "\n"
        return s

    def toStringConMosse(self):
        s = "---------inizio stato----------------\n"
        for i, r in enumerate(self.rods, start=1):
            s += f"paletto {str(i)}\n{r.toString()}\n"
        s += "\n"
        s+= "mosse "+str(self.g)+"\n"
        s += "---------fine stato----------------\n"
        return s
    
    def aP_C_Caller(self, mat_a, max_d):
        return aP_C(mat_a, max_d, self.rods)
    
    
    def aP(self, mat_a, max_d):
        
        mat = np.array(mat_a)

        for i in range(len(self.rods)):
            for j in range(len(self.rods)):
                if(i<j):
                    '''lp = LineProfiler()
                    lp_wrapper = lp(self.__aPCalculation)
                    lp_wrapper(mat, i, j, max_d)
                    lp.print_stats()'''
                    self.__aPCalculation1(mat, i, j, max_d) 

        return mat
    
    def aPRulesCalculation(self, mat, action):
        mat[action.j, action.i] = 0
        return mat
    
    
    """
    Calcola la matrice di adiacenza pesata A tra le diverse configurazioni.

    Parametri:
        mat (matrice): La matrice di adiacenza da popolare
        i (int): L'indice della riga corrente
        j (int): L'indice della colonna corrente

    Questa funzione controlla se le aste i e j hanno entrambe un disco. 
    In caso affermativo, confronta gli ultimi dischi delle due aste.
    Se il disco i è più piccolo del disco j, imposta il valore mat[i,j] a 0 per indicare
    che non è possibile spostare il disco i sul disco j.
    Altrimenti lascia il valore di mat[i,j] invariato.

    Se una delle due aste non ha dischi, mat[i,j] viene impostato a 0.
    """
    def __aPCalculation1(self, mat, i, j, max_d):
        
        #check if the node is empty
        if self.rods[i].hasDisk():
            if self.rods[j].hasDisk():

                if(self.rods[i].getLast()[0] == self.rods[j].getLast()[0]):
                    boo = 0
                elif self.rods[i].getLast()[0] > self.rods[j].getLast()[0]:
                    boo = 1
                else:
                    boo = -1

                if boo==1:
                    mat[i, j] = 0
                if boo==-1:
                    mat[j, i] = 0
                if (self.rods[i].stackLen() == 1 and self.rods[j].stackLen() == 1) and (self.rods[i].getLast()[0] == max_d and self.rods[j].getLast()[0] == max_d):
                    mat[i, j] = 0
                    mat[j, i] = 0
            else:
                mat[j, i] = 0
        else:
            mat[i, j] = 0
        if not self.rods[j].hasDisk():
            mat[j, i] = 0
    
    def __aPCalculation(self, mat, i, j, max_d):
        #check if the node is empty
        if not (i == j or not self.rods[i] or not self.rods[i].hasDisk()):
            if not (not self.rods[j] or not self.rods[j].hasDisk() or self.rods[i].getLast().compare(self.rods[j].getLast()) != 1):
                mat[i, j] = 0
            if (self.rods[i].stackLen() == 1 and self.rods[j].stackLen() == 1) and (self.rods[i].getLast()[0] == max_d and self.rods[j].getLast()[0] == max_d):
                mat[i, j] = 0
        else:
            mat[i, j] = 0

    
    def calculateHeuristic3C_OP(self, goal):
        c1 = goal.rods[0]._Rod__stack[0][1]
        c2 = goal.rods[1]._Rod__stack[0][1]
        c = [c1, c2]
        max_d = goal.rods[0]._Rod__stack[0][0]
        #print(self.toString_())
        return heutristicCalc(self.rods, goal.rods, max_d, c)

    
    def calculateHeuristic4(self, goal):
        return sum(self.rods[i].compareRods4(goal.rods[i], i) for i in range(len(self.rods)))
    
    def setgValue(self, _g):
        self.g = int(_g)


    def stateClone(self, i, j):

        """ c_rods = [r.rodClone() for r in self.rods] """

        c_rods = list(self.rods)

        c_rods[i] = self.rods[i].rodClone()
        c_rods[j] = self.rods[j].rodClone()

        c_g = self.g

        return State(c_rods, c_g)