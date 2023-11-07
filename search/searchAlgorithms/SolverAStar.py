# Implements the function t (result)
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from searchAlgorithms.OpenList import OpenList
import datetime

from model.Node import Node
from model.Action import Action
#from searchAlgorithms.SolverAStarC_lib import expandC

"""
classe che definisce:
    - solve: algoritmo di esplorazione dell'albero
    - isGoal: funzione che verifica se uno stato è il goal
    - expand: funzione che dato un nodo genera tutti i nodi figli
    - newNode: metodo tecnico che crea un nuovo nodo
"""

class SolverAStar:

    #====================================================================================================

    def __init__(self, world) -> None:
        self.world = world
        self.start_time = datetime.datetime.now()

    #====================================================================================================
  
    def solve(self, max_d, heuristic_type = 3) -> Node:
        
        #self.file = open("ce3.txt", mode = 'w' , encoding='utf-8')
        
        self.max_d = max_d

        #Choose heuristic_type

        if(heuristic_type == 4):
            self.calculateHeuristic = self.calculateHeuristic4

        r = len(self.world.goal.rods)
        frontier = OpenList(r)
        frontier.add_item(self.world.start_node, 0)

        reached = {self.world.start_node.state} #empty set explored

        expanded_nodes = 0
        limit = pow(7, max_d)

        # Uncomment this lines if you want to see the number of nodes expanded / second - (Part 1/2)
        """start_time = datetime.datetime.now()
        al_nod=0"""


        while not frontier.is_empty(): #until frontier is empty
            n = frontier.pop_item()
            reached.add(n[0].state)
            expanded_nodes+=1
       
            # Uncomment this lines if you want to see the number of nodes expanded / second - (Part 2/2)
            """tim = datetime.datetime.now() - start_time
            if (int((tim).total_seconds()) != 0 and int((tim).total_seconds()) % 7 == 0):
                
                start_time = datetime.datetime.now()
                print(
                    f" Expanded Nodes:{expanded_nodes} - Speed:{(expanded_nodes-al_nod)/tim.total_seconds()}"
                )
                al_nod=expanded_nodes"""

            if (expanded_nodes % limit == 0):
                print(
                    f" Expanded Nodes:{expanded_nodes}"
                )

            
            for child in self.expand(n[0]):
                in_frontier = child in frontier

                if (not in_frontier) and not child.state in reached: 
                    if (self.isGoal(child.state)):
                        print(f" Total Expanded Nodes:{expanded_nodes}")
                        #self.file.close()
                        return child
                    frontier.add_item(child, child.e+child.g)
                    
                elif in_frontier:
                    d = frontier.extract_item(child)
                    if(child < d[1]):
                        frontier.remove_item(d[1])
                        frontier.add_item(child, child.e+child.g)
            
        return None 
    
    #====================================================================================================

    def isGoal(self, state):
        return self.world.goal == state
    
    #====================================================================================================

    def expand(self, node):
        s = node.state
        mat = s.aP_C_Caller(self.world.a, self.max_d)
        mat = s.aPRulesCalculation(mat, node.action)
        nodes = []

        for i in range(len(mat)):
            for j in range(len(mat)):         
                if mat[i, j] == 1:
                    self.newNode(nodes, node, i, j)

        return nodes
    
    #====================================================================================================
    
    def newNode(self, nodes, parent, i, j):
        g = self.calculateCost(parent.g)
        s = parent.state.stateClone(i, j)
        s1 = self.result(s, i, j)
        s1.setgValue(g)
        e = self.calculateHeuristic(s1)
        action_new = Action(i,j)
    
        nodes.append(Node(s1, action_new, parent, s1.g, e))

    #====================================================================================================
  
    def result(self, stato_partenza, i, j):
        d1 = stato_partenza.rods[i].remDisk()
        stato_partenza.rods[j].addDisk(d1)
        return stato_partenza
    
    #====================================================================================================

    def calculateCost(self, g):
        return g + 1
    
    #====================================================================================================
    #Heuristics

    def calculateHeuristic(self, s1):
        return s1.calculateHeuristic3C_OP(self.world.goal)

    def calculateHeuristic4(self, s1):
        return s1.calculateHeuristic4(self.world.goal)
     
    #====================================================================================================

    def write_log_file(self, n1, stato_ragg):
        self.file.write("stato in reached:\n")
        self.file.write(stato_ragg.toStringConMosse())
        self.file.write("stato generato:\n")
        self.file.write("ultima azione: "+n1.action.toString()+"\n")
        self.file.write(n1.state.toStringConMosse()+"\n")
        self.file.write("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n")

    #====================================================================================================