import numpy as np

class World:

    def __init__(self, start_node, goal, rods_number) -> None:
        self.start_node = start_node
        self.goal = goal
        self.rods_number = rods_number

        self.a = self.initActionMatrix()

        #print(self.a)


    # Rows are the starting point and coloums are the end point
    def initActionMatrix(self):
        init_1 = "".join("1 " for _ in range(self.rods_number-1))
        init_mat = f"0 {init_1};"

        for i in range(self.rods_number-1):
            init_mat += f'{init_1[:2 * i + 1]} 0{init_1[2 * i + 1:]};'

        init_mat=init_mat.replace(" ;",";")
        return np.matrix(init_mat[:-1])
    