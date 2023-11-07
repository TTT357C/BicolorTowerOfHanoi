from World import World as W
from Node import Node
from State import State
from Rod import Rod
from Action import Action
from Disk import Disk
import datetime

# TODO Rename this here and in `fourDisks`
def createTower4(coloreBase, altroColore):
    result = Rod()

    result.addDisk(Disk(coloreBase, 4))
    result.addDisk(Disk(altroColore, 3))
    result.addDisk(Disk(coloreBase, 2))
    result.addDisk(Disk(altroColore, 1))

    return result

def createTower3(coloreBase, altroColore):
    result = Rod()

    result.addDisk(Disk(coloreBase, 3))
    result.addDisk(Disk(altroColore, 2))
    result.addDisk(Disk(coloreBase, 1))

    return result



def createTower(coloreBase, altroColore, numDisk):
    result = Rod()

    for i in range(numDisk):
        if(i % 2==0):
            result.addDisk(Disk(coloreBase, numDisk - i))
        else:
            result.addDisk(Disk(altroColore, numDisk - i))
        
    return result


def createUniformColor(colore, numDisk):
    result = Rod()

    for i in range(numDisk):
        result.addDisk(Disk(colore, numDisk - i))
        
    return result


def statoIniziale(numPaletti, numDisk, cBaseSx, cBaseDx):
    
    paletti = []
    for i in range(numPaletti):
        if(i <= 1):
            if(i == 0):
                paletti.append(createTower(cBaseSx, cBaseDx, numDisk))
            if(i == 1):
                paletti.append(createTower(cBaseDx, cBaseSx, numDisk))
        else:
            paletti.append(Rod())
    return paletti


def statoFinale(numPaletti, numDisk, cBaseSx, cBaseDx):
    paletti = []
    for i in range(numPaletti):
        if(i <= 1):
            if(i == 0):
                paletti.append(createUniformColor(cBaseSx, numDisk))
            if(i == 1):
                paletti.append(createUniformColor(cBaseDx, numDisk))
        else:
            paletti.append(Rod())
    return paletti


rod = createUniformColor("white", 4)
rod2 = createTower("white", "red", 5)

stato_iniziale = State(statoIniziale(3, 4, "white", "red"))
stato_finale = State(statoFinale(3,3, "red", "white"))

print( stato_iniziale.calculateHeuristic2(stato_finale) ) 