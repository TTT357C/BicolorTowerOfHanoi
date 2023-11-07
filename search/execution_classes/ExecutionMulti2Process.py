
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import multiprocessing
import time

from searchAlgorithms.SolverAStar import SolverAStar as S
from creation_classes.WorldCreation import WorldCreation as wc


class Color:
    colors = []


def startExecutionMiddle(_n, c, ret):

    Color.colors.append(c[0])
    Color.colors.append(c[1])

    world = wc(Color).createWorldMCorr(_n)

    n = S(world).solve(_n)

    ret[1] = extract_solution_node(n) 

    
def startExecutionFirst(_n, c, ret):

    Color.colors.append(c[0])
    Color.colors.append(c[1])
    
    world = wc(Color).createWorldFirstTowerCorr(_n)
    
    n = S(world).solve(_n,4)

    ret[0] = extract_solution_node(n)
    print(n.g)



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

def runner(c,n):

    Color.colors = c

    if(len(Color.colors) == 0):
        Color.colors.append("red")
        Color.colors.append("black")
         

    start_time = time.time()
    manager = multiprocessing.Manager()
    return_dict = manager.dict()

    t1 = multiprocessing.Process(target = startExecutionFirst, args=[n, c, return_dict])
    t1.start()
       
    t2 = multiprocessing.Process(target = startExecutionMiddle, args=[n, c, return_dict])
    t2.start()

    t1.join()
    t2.join()
    
    t1.terminate()
    t2.terminate()

    s = return_dict[1] + return_dict[0]
    s1 = ""
    num_moves = 0
    #try:
    for node in s:
            if(not node.action.isnull()):
                num_moves+= 1

    s1 = f"Numero di Mosse: {num_moves}\n" 
    
    print(f"--- {time.time() - start_time} seconds ---")
    print(s1)

    return s


if __name__ == "__main__":
    runner([],5)