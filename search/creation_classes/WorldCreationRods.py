from model.World import World as W
from model.Node import Node
from model.State import State
from model.Rod import Rod
from model.Action import Action
from creation_classes.TowerCreation import TowerCreation


class WorldCreationRods:

    def __init__(self, c) -> None:
        self.color = c
        self.tc = TowerCreation()


    def createWorldSameBase(self,numD):
        rod = self.tc.createTower(self.color.colors[0], self.color.colors[1], numD)
        rod2 = self.tc.createTower(self.color.colors[1], self.color.colors[0], numD)

        rod3 = self.tc.createTower(self.color.colors[0], self.color.colors[0], numD)
        rod4 = self.tc.createTower(self.color.colors[1], self.color.colors[1], numD)

        init_state = [rod,rod2,Rod()]
        goal = [rod3,rod4,Rod()]

        return W(Node(State(init_state,0),Action(0,0)),State(goal,100000),len(init_state))


    def createWorld(self, numD):
        rod = self.tc.createTower(self.color.colors[0], self.color.colors[1], numD)
        rod2 = self.tc.createTower(self.color.colors[1], self.color.colors[0], numD)

        rod3 = self.tc.createTower(self.color.colors[1], self.color.colors[1], numD)
        rod4 = self.tc.createTower(self.color.colors[0], self.color.colors[0], numD)

        init_state = [rod,rod2,Rod(),Rod()]
        goal = [rod3,rod4,Rod(),Rod()]

        return W(Node(State(init_state,0),Action(0,0)),State(goal,100000),len(init_state))
