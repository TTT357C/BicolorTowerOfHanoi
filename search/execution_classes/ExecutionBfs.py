import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from searchAlgorithms.SolverBfs import SolverBfs
from creation_classes.WorldCreation import WorldCreation as wc

class Color:
    colors = []

def startExecution(c,n_disk,n_rods = 3):

    Color.colors = c

    world = wc(Color).createWorld(n_disk,n_rods)

    #n = Sbfs(world).solve(_n,"")
    n = SolverBfs(world).solve(n_disk)

    s=""
    if n is not None:
        solution = extract_solution(n)

        solution.reverse()
        s = f"Numero di Mosse: {len(solution)}\n"

        s += "".join(a.toString()+"\n" for a in solution)
    else:
        s += "Unsolvable"


    return extract_solution_node(n)


#copiati e incollati da Execute.py
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

