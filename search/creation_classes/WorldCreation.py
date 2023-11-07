from model.World import World as W
from model.Node import Node
from model.State import State
from model.Rod import Rod
from model.Action import Action
from creation_classes.TowerCreation import TowerCreation


class WorldCreation:

    def __init__(self, c) -> None:
        self.color = c
        self.tc = TowerCreation()

    def createWorldMP(self,numD):
        #First sub-goal
        rod = self.tc.createSingleBase(self.color.colors[0], numD)
        rod2 = self.tc.createBigTower(self.color.colors[1], self.color.colors[0], numD)

        #Second sub-goal
        rod3 = self.tc.createSingleBase(self.color.colors[1], numD)
        rod4 = self.tc.createBigMiddleTower(self.color.colors[0], self.color.colors[1], numD)

        init_state = [Rod(),rod2,rod]
        goal = [rod3,Rod(),rod4]

        return W(Node(State(init_state,0),Action(0,0)),State(goal,100000),len(init_state))
    
    def createWorldMA(self,numD):
        #First sub-goal
        rod = self.tc.createSingleBase(self.color.colors[1], numD)
        rod2 = self.tc.createBigMiddleTower(self.color.colors[0], self.color.colors[1], numD)

        #Second sub-goal
        rod3 = self.tc.createSingleBase(self.color.colors[0], numD)
        rod4 = self.tc.createBigEndTower2(self.color.colors[1], self.color.colors[0], numD)

        init_state = [rod,Rod(),rod2]
        goal = [rod4,rod3,Rod()]

        return W(Node(State(init_state,0),Action(0,0)),State(goal,100000),len(init_state))

    def createWorldM(self,numD):
        #First sub-goal
        rod = self.tc.createSingleBase(self.color.colors[0], numD)
        rod2 = self.tc.createBigTower(self.color.colors[1], self.color.colors[0], numD)

        #Second sub-goal
        rod3 = self.tc.createSingleBase(self.color.colors[0], numD)
        rod4 = self.tc.createBigEndTower(self.color.colors[1], self.color.colors[0], numD)

        init_state = [Rod(),rod2,rod]
        goal = [rod4,rod3,Rod()]

        return W(Node(State(init_state,0),Action(0,0)),State(goal,100000),len(init_state))

    def createWorldMCorr(self,numD):
        #First sub-goal
        rod = self.tc.createSingleBase(self.color.colors[0], numD)
        rod2 = self.tc.createBigTower(self.color.colors[1], self.color.colors[0], numD)

        rod3 = self.tc.createTower(self.color.colors[1], self.color.colors[1], numD)
        rod4 = self.tc.createTower(self.color.colors[0], self.color.colors[0], numD)

        init_state = [Rod(),rod2,rod]
        goal = [rod3,rod4,Rod()]

        return W(Node(State(init_state,0),Action(0,0)),State(goal,100000),len(init_state))


    def createWorldFirstTower(self,numD):
        #Inital State
        rod = self.tc.createTower(self.color.colors[0], self.color.colors[1], numD)
        rod2 = self.tc.createTower(self.color.colors[1], self.color.colors[0], numD)

        #First sub-goal
        rod3 = self.tc.createSingleBase(self.color.colors[0], numD)
        rod4 = self.tc.createBigTower(self.color.colors[1], self.color.colors[0], numD)

        init_state = [rod,rod2,Rod()]
        goal = [Rod(),rod4,rod3]

        return W(Node(State(init_state,0),Action(0,0)),State(goal,100000),len(init_state))

    def createWorldFirstTowerCorr(self,numD):
        #Inital State

        #crea rod di numd dischi a colori alternati
        rod = self.tc.createTower(self.color.colors[0], self.color.colors[1], numD)
        rod2 = self.tc.createTower(self.color.colors[1], self.color.colors[0], numD)

        #First sub-goal
        rod3 = self.tc.createSingleBase(self.color.colors[0], numD)
        rod4 = self.tc.createBigTower(self.color.colors[1], self.color.colors[0], numD)

        init_state = [rod,rod2,Rod()]
        goal = [Rod(),rod4,rod3]

        return W(Node(State(init_state,0),Action(0,0)),State(goal,100000),len(init_state))


    def createWorldLastTower(self,numD):
        
        rod = self.tc.createSingleBase(self.color.colors[0], numD)
        rod2 = self.tc.createBigEndTower(self.color.colors[1], self.color.colors[0], numD)

        rod3 = self.tc.createTower(self.color.colors[0], self.color.colors[0], numD)
        rod4 = self.tc.createTower(self.color.colors[1], self.color.colors[1], numD)

        init_state = [rod2,rod,Rod()]
        goal = [rod4,rod3,Rod()]

        return W(Node(State(init_state,0),Action(0,0)),State(goal,100000),len(init_state))
    
    def createWorldLastTower2(self,numD):
        
        rod = self.tc.createSingleBase(self.color.colors[1], numD)
        rod2 = self.tc.createBigEndTower(self.color.colors[0], self.color.colors[1], numD)

        rod3 = self.tc.createTower(self.color.colors[0], self.color.colors[0], numD)
        rod4 = self.tc.createTower(self.color.colors[1], self.color.colors[1], numD)

        init_state = [rod,rod2,Rod()]
        goal = [rod4,rod3,Rod()]

        return W(Node(State(init_state,0),Action(0,0)),State(goal,100000),len(init_state))


    def createWorldSameBase(self,numD):
        rod = self.tc.createTower(self.color.colors[0], self.color.colors[1], numD)
        rod2 = self.tc.createTower(self.color.colors[1], self.color.colors[0], numD)

        rod3 = self.tc.createTower(self.color.colors[0], self.color.colors[0], numD)
        rod4 = self.tc.createTower(self.color.colors[1], self.color.colors[1], numD)

        init_state = [rod,rod2,Rod()]
        goal = [rod3,rod4,Rod()]

        return W(Node(State(init_state,0),Action(0,0)),State(goal,100000),len(init_state))


    def createWorld(self, numD, n_rods):
        rod = self.tc.createTower(self.color.colors[0], self.color.colors[1], numD)
        rod2 = self.tc.createTower(self.color.colors[1], self.color.colors[0], numD)

        rod3 = self.tc.createTower(self.color.colors[1], self.color.colors[1], numD)
        rod4 = self.tc.createTower(self.color.colors[0], self.color.colors[0], numD)

        init_state = [rod,rod2,Rod()]
        goal = [rod3,rod4,Rod()]

        for _ in range(3,n_rods):
            init_state.append(Rod())
            goal.append(Rod())

        return W(Node(State(init_state,0),Action(0,0)),State(goal,100000),len(init_state))
