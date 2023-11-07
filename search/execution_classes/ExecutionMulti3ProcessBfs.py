
import multiprocessing
import os
import sys
import time

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from searchAlgorithms.SolverBfs import SolverBfs as S
from creation_classes.WorldCreation import WorldCreation as wc

class Color:
    colors = []

def startExecutionSTART(_n,c,ret):

    Color.colors.append(c[0])
    Color.colors.append(c[1])

    world = wc(Color).createWorldFirstTower(_n)

    #n = S(world).solve(_n,"")
    n = S(world).solve(_n)

    solution = extract_solution2(n)

    solution.reverse()
    s = f"Numero di Mosse Start: {n.g}\n"

    s += "".join(a.toString()+"\n" for a in solution)

    ret[0] = extract_solution_node(n)

def startExecutionMIDDLE(_n,c,ret):

    Color.colors.append(c[0])
    Color.colors.append(c[1])

    world = wc(Color).createWorldM(_n)

    #n = S(world).solve(_n,"")
    n = S(world).solve(_n)

    solution = extract_solution(n)

    solution.reverse()
    s = f"Numero di Mosse Middle: {n.g}\n"

    s += "".join(a.toString()+"\n" for a in solution)

    ret[1] = extract_solution_node(n)

def startExecutionEND(_n,c,ret):

    Color.colors.append(c[0])
    Color.colors.append(c[1])

    world = wc(Color).createWorldLastTower(_n)

    #n = S(world).solve(_n,"")
    n = S(world).solve(_n)

    solution = extract_solution3(n)

    solution.reverse()
    s = f"Numero di Mosse End: {n.g}\n"

    s += "".join(a.toString()+"\n" for a in solution)
  
    ret[2] = extract_solution_node(n)

#====================================================================================================
def extract_solution(n):
        solution = []
        while n.parent is not None:
            solution.append(n.action)
            n = n.parent
        return solution

def extract_solution2(n):
        solution = []
        while n.parent is not None:
            solution.append(n.action)
            n = n.parent
        return solution

def extract_solution3(n):
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
#====================================================================================================

def runner(c,n):

    start_time = time.time()

    manager = multiprocessing.Manager()
    return_dict = manager.dict()

    t1 = multiprocessing.Process(target = startExecutionMIDDLE, args=[n,c,return_dict])
    t1.start()

    t2 = multiprocessing.Process(target = startExecutionSTART, args=[n,c,return_dict])
    t2.start()

    t3 = multiprocessing.Process(target = startExecutionEND, args=[n,c,return_dict])
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    t1.terminate()
    t2.terminate()
    t3.terminate()

    s = return_dict[2] + return_dict[1] + return_dict[0]

    num_moves = sum(not node.action.isnull() for node in s)

    s1 = f"Numero di Mosse: {num_moves}\n"

    print(s1)


    print(f"--- {time.time() - start_time} seconds ---")

    return s

if __name__ == "__main__":
    runner(["red","white"],7)