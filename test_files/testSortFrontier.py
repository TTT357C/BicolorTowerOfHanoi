from State import State
from Node import Node
from Action import Action
from Rod import Rod
from Disk import Disk
from creation_classes.WorldCreation import WorldCreation as wc

frontier = [] 
frontier.append(Node(None, None, None, 0, 5))
frontier.append(Node(None, None, None, 1, 5))
frontier.append(Node(None, None, None, 3, 5))



n1  = Node(None, None, None, 1, 7)
cal = (n1.e - n1.g)
cont = -1

for i in frontier:
    cont+=1
    if (i.e - i.g) >= cal:
        break
    
frontier.insert(cont, n1)



print(frontier.pop().g)