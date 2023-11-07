import sys
sys.path.insert(0, 'C:\AI_prog\IntelligentSystemProject\search\model')
sys.path.insert(0, 'C:\AI_prog\IntelligentSystemProject\search\creation_classes')
from TowerCreation import TowerCreation
from World import World as W
from Node import Node
from State import State
from Rod import Rod
from Action import Action
from Disk import Disk
import time

class G:
    def __init__(self) -> None:
        self.tc = TowerCreation()

    def gol(self, numD):
        rod3 = self.tc.createTower("c2", "c2", numD)
        rod4 = self.tc.createTower("c1", "c1", numD)

        return State([rod3,rod4,Rod()], 10000000000000000000)  
    
    def init(self, numD):
        rod3 = self.tc.createTower("c1", "c2", numD)
        rod4 = self.tc.createTower("c2", "c1", numD)

        return State([rod3,rod4,Rod()], 10000000000000000000)  

g = G()


d11 = Disk("c1", 5)
d12 = Disk("c2", 4)
d13 = Disk("c1", 3)
d14 = Disk("c2", 2)
d15 = Disk("c1", 1)
d16 = Disk("c2", 1)

d11 = Disk("c2", 5)
d12 = Disk("c1", 4)
d23 = Disk("c2", 3)
d24 = Disk("c1", 2)

r1 = Rod()
r1.addDisk(d11)
r1.addDisk(d12)
r1.addDisk(d13)
r1.addDisk(d14)
r1.addDisk(d15)
r1.addDisk(d16)

r2 = Rod()

r3 = Rod()
r3.addDisk(d21)
r3.addDisk(d22)
r3.addDisk(d23)
r3.addDisk(d24)



rs = [r1,r2,r3]
ss = State(rs, 4)

gg = g.gol(3)
ii = g.init(3)

print("ss:\n"+ss.toString_())
print(gg.toString_())

""" print("e1:"+ str(ss.calculateEuristic1(gg)))
print("e2:"+ str(ss.calculateEuristic2(gg)))
print("e3:"+ str(ss.calculateEuristic3(gg)))
print("e4:"+ str(ss.calculateEuristic4(gg))) """

start = time.time()

print("e4:"+ str(ss.calculateHeuristic4(gg)))

end = time.time()
print(end - start)