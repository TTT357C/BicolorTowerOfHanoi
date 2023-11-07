import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from PDDL.pythonWriterPLUS.WriteInitPDDL import scriviInitPDDL
from PDDL.pythonWriterPLUS.WriteGoalPDDL import scriviGoalPDDL


path = 'PDDL_Data\\GenproblemHanoi.pddl'
# Sets the path to the PDDL file that will be written
#path = 'C:/AI_PDDL_study/pythonPDDL/problemHanoi.pddl'

#=====================================================================================================

"""
WritePDDL class handles writing the initial and goal states to a PDDL file.
The write() method takes in parameters for the number of disks, rods, and colors,
and uses those to generate the problem name, call the initial state writer,
and call the goal state writer based on parity of disks.
"""
class WritePDDL:


    """
    Write the initial and goal PDDL states to a file.
        
        Parameters:
           num_disk: Number of disks to generate
           num_rods: Number of rods to generate 
           col1: Color for disks starting on rod 1
           col2: Color for disks starting on rod 2
        
        Returns: None
    """
    def write(num_disk, num_rods):
        
        col1 = "w"
        col2="r"
        p_name = f"move_r{str(num_disk)}_to_goal"
        d_name = "hanoiPLUS"

        init_writer = scriviInitPDDL(path, col1, col2)
        init_writer.write_initial_state(p_name, d_name,num_disk, num_rods)

        if(num_disk%2 == 0):
            goal_writer = scriviGoalPDDL(path, num_disk, num_rods, col1, col2)

        else:
            goal_writer = scriviGoalPDDL(path, num_disk, num_rods, col2, col1)

        goal_writer.write_goal_state()

#=====================================================================================================

if __name__ == "__main__":
    # If run as a script, prompt for number of disks and rods, initialize colors,
    # and call WritePDDL.write() to generate the PDDL file.
    num_disk = int(input("number of disks: "))
    num_rods = int(input("number of rods: "))

    col1 = "r"
    col2 = "w"
    WritePDDL.write(num_disk,num_rods,col1,col2)

