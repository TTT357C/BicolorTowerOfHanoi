
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from searchAlgorithms.SolverAStar import SolverAStar as S
from creation_classes.WorldCreation import WorldCreation as wc


class Color:
    colors = []


def startExecution(c,_n,n_rods = 3):

    Color.colors = c
    
    world = wc(Color).createWorld(_n,n_rods)

    #creazione oggetto che contiene stato inziale e goal da risolvere.
    #world = wc(Color).createWorldFirstTowerCorr(_n)#subgoal in 2 thread (init->sg)
    #world = wc(Color).createWorldMCorr(_n)#subgoal in 2 thread (sg->g)
    
    n = S(world).solve(_n)
  

    s = extract_solution_node(n)
    s1 = ""
    num_moves = 0
    for node in s:
        if(not node.action.isnull()):
            num_moves+= 1

    s1 += "Numero di Mosse: {"+str(s[0].g)+"}\n"

    """ for i in range(1,len(s)):
        s1 += s[len(s)-i].action.toString()+"\n"

        s1 = s1.replace("1 --> 1\n", "") """
        
    #print("secondi:")
    #print(int(elapsed.total_seconds()))
    #TODO rimuovere
    print(s1)
    

    return extract_solution_node(n)

def extract_solution(n):
        solution = []
        while n.parent is not None:
            solution.append(n.action)
            n = n.parent
        return solution

def extract_solution_node(n):
        solution = []
        while n.parent is not None:
            solution.append(n)
            n = n.parent
        solution.append(n)
        return solution

if __name__ == "__main__":
    Color.colors.append("c1")
    Color.colors.append("c2")
    startExecution(Color.colors,4)

