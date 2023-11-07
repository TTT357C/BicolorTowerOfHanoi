from State import State
from Node import Node
from Action import Action
from Rod import Rod
from Disk import Disk


def createTower(base, secondo, numD):
    result = Rod()

    for i in range(numD):
        if(i % 2==0):
            result.addDisk(Disk(base, numD - i))
        else:
            result.addDisk(Disk(secondo, numD - i))
        
    return result

numD = 3
rod = createTower("w", "r", numD)
rod2 = createTower("r", "w", numD)

rods = [rod,rod2,Rod()]

stato_raggiunto = State(rods, 5)
stato_nuovo = State(rods, 3)

print(stato_raggiunto == stato_nuovo)

reached = {stato_raggiunto}

value_ =  {stato_nuovo} & reached 
stato_preso = value_.pop()
print(stato_preso.toString())
print(stato_preso.g)

reached.remove(stato_nuovo)
reached.add(stato_nuovo)
print("t")