import datetime
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent+"\model")
from queue import LifoQueue

from model.Node import Node
from model.Action import Action


"""
classe che definisce:
    - solveDfs: metodo che esplora il search algorithm con l'algoritmo di DFS
    - isGoal: funzione che verifica se uno stato è il goal
    - expand: funzione che dato un nodo genera tutti i nodi figli
    - newNode: metodo tecnico che crea un nuovo nodo dato il nodo padre e un'azione come input
"""

class SolverDfs:


    def __init__(self, world) -> None:
        self.world = world
        self.start_time = datetime.datetime.now()
           
    
    def solve(self, max_d) -> list:
        self.max_d = max_d

        frontier = LifoQueue()
        frontier.put(self.world.start_node)
        nods_in_frontier = {self.world.start_node}
        reached = {self.world.start_node.state}

        expanded_nodes = 0
        limit = pow(7, self.max_d)
        
        while frontier: #finche la frontiera non vuota
            
            n = frontier.get()
            nods_in_frontier.remove(n)
            expanded_nodes+=1
            reached.add(n.state)
            counter+=1
            
            if (expanded_nodes % limit == 0):
                print(
                    f" Expanded Nodes:{expanded_nodes} - Frontier length: {len(frontier)} - Reached length: {len(reached)}"
                )

            for child in self.expand(n):
            
                if  (not child.state in reached) and (not child in nods_in_frontier): 
                    if (self.isGoal(child.state)):
                        print(f" Total Expanded Nodes:{expanded_nodes}")
                        #self.file.close()
                        return child
                    
                    frontier.append(child)
                    nods_in_frontier.add(child)
        return None #return false
    

    #====================================================================================================

    def expand(self, node):
        s = node.state
        mat = s.aP(self.world.a, self.max_d)
        mat = s.aPRulesCalculation(mat, node.action)
        nodes = []

        for i in range(len(mat)):
            for j in range(len(mat)):
                
                if mat[i, j] == 1:
                    self.newNode(nodes, node, i, j)


        return nodes
        
    #====================================================================================================

    def isGoal(self, state):
        return self.world.goal == state
    
    #====================================================================================================
    
    def result(self, stato_partenza, i, j):
        d1 = stato_partenza.rods[i].remDisk()
        stato_partenza.rods[j].addDisk(d1)
        return stato_partenza

    #====================================================================================================

    def calculateCost(self, g):
        return g + 1

    #====================================================================================================

    def newNode(self, nodes, parent, i, j):
        g = self.calculateCost(parent.g)
        s = parent.state.stateClone(i, j)
        s1 = self.result(s, i, j)
        s1.setgValue(g)
        nodes.append(Node(s1, Action(i,j), parent, s1.g, 0))

    #====================================================================================================
    
    def presentaFrontiera(self, frontiera):
        print("FRONTIERA")
        num = 1
        for i in frontiera:
            print(f"[] nodo {str(num)}")
            print(i.toString())
            num= num+1   
