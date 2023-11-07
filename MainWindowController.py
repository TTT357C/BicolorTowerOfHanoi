import datetime
from multiprocessing import Manager, Process
from tkinter import colorchooser
from search.execution_classes import ExecutionMulti2Process as ExecutionMulti2Process
from search.execution_classes import ExecutionMulti3Process as ExecutionMulti3Process
from search.execution_classes import ExecutionMulti3ProcessBfs as ExecutionMulti3ProcessBfs
from search.execution_classes import ExecutionBfs as ExecutionBfs
from search.execution_classes import Execution as Execution
from PDDL.pythonWriterPLUS.WritePDDL import WritePDDL
from WaitingWindow import WaitingWindow as waitw
from ResultWindow import ResultWindow as resw
from search.infomessage.Message import Message
from PDDL.ShellCommand import ShellCommand

"""
    This class work as a controller for MainWindow
"""

#====================================================================================================
"""
    __starter starts the execution based on the selected algorithm.
    
    It takes in the return dictionary to store results, number of disks, 
    number of rods, selected algorithm, and number of rods. 
    
    It times the execution, runs the selected algorithm, stores results in the
    return dictionary, and stores the elapsed time. Handles errors if invalid
    algorithm selected.
"""
def __starter(return_dict,c,n,selected_g,n_rods):
    
    
    start_time = datetime.datetime.now()
    if(selected_g == 0):
        return_dict[0] = Execution.startExecution(c,n,n_rods)
    elif(selected_g == 1):
        return_dict[0] = ExecutionMulti2Process.runner(c,n)
    elif(selected_g == 2):
        return_dict[0] = ExecutionBfs.startExecution(c,n,n_rods)
    elif(selected_g == 3):
        return_dict[0] = ExecutionMulti3Process.runner(c,n)
    elif(selected_g == 4):
        return_dict[0] = ExecutionMulti3ProcessBfs.runner(c,n)
    else:
        t1 = Process(target = Message, args=(Message.ERROR,"Error","404"))
        t1.start()
    
    return_dict[1] = datetime.datetime.now() - start_time
    return 

#====================================================================================================

"""
    Runs the PDDL planner to find a solution for the n-disk Towers of Hanoi problem.
    
    Writes the PDDL domain and problem files using WritePDDL.write(), then executes the ENHSP planner 
    to find a solution. Stores the planner output and elapsed time in the return_dict dictionary.
    
    Parameters:
       return_dict: Dictionary to store planner output and elapsed time
       n: Number of disks to solve for
    e.colors = colors
"""
def __starter2(return_dict,n):
     

    #TODO Magic Number
    WritePDDL.write(n,4)
    
    start_time = datetime.datetime.now()
    return_dict[0] = ShellCommand().run(["java","-jar","PDDL_Data/enhsp-20.jar","-o","PDDL_Data/domainHanoiPLUS.pddl","-f","PDDL_Data/GenproblemHanoi.pddl","-planner","opt-hrmax"])
    return_dict[1] = datetime.datetime.now() - start_time
    return 

#====================================================================================================

"""
    Runs the ENHSP planner to find a solution for the n-disk Towers of Hanoi problem using subgoal decomposition.
    
    Writes the initial state and subgoal PDDL files, executes the ENHSP planner, 
    and stores the planner output and elapsed time in the return_dict dictionary.
    
    Parameters:
       return_dict: Dictionary to store planner output and elapsed time  
       type_of_PDDL: Name of PDDL file to use for subgoal planning
"""

def __starter3(return_dict, type_of_PDDL):
    
    #e.colors = colors
    return_dict[0] = ShellCommand().run(["java","-jar","PDDL_Data/enhsp-20.jar","-o","PDDL/subgoals_PDDL/domainHanoiPLUS.pddl","-f","PDDL/subgoals_PDDL/"+type_of_PDDL+"","-planner","opt-hrmax"])
    return 

#====================================================================================================


"""
    Runs the ENHSP planner to find a solution for the n-disk Towers of Hanoi problem 
    using subgoal decomposition, for n between 4 and 6.

    Launches multiple processes to generate the initial state and subgoal PDDL files, 
    execute the ENHSP planner on them, and collect the outputs. 

    Returns the combined planner output and elapsed time.
"""
def runPDDLMulti(number):
# 

    if(number >= 4 and number <=6):

        t2 = Process(target = waitw, args=())
        t2.start()

        INIT_SUB = ["init-subG4.pddl","init-subG5.pddl","init-subG6.pddl"]
        SUB_GOAL = ["sub-goal4.pddl","sub-goal5.pddl","sub-goal6.pddl"]

        manager = Manager()
        return_dict = manager.dict()
        return_dict2 = manager.dict()
        start_time = datetime.datetime.now()
        t1 = Process(target = __starter3, args=(return_dict,INIT_SUB[number-4]))
        t3 = Process(target = __starter3, args=(return_dict2,SUB_GOAL[number-4]))
        t1.start()
        t3.start()
        t1.join()
        t3.join()
        t2.terminate()
        t1.terminate()
        t3.terminate()

        t4 = Process(target = resw, args=("PDDLMulti:\n" + return_dict[0] + return_dict2[0], datetime.datetime.now() - start_time))
        t4.start()

#====================================================================================================

"""
    Runs the ENHSP planner to find a solution for the n-disk Towers of Hanoi problem.

    Launches a process that runs the ENHSP planner.

    Return the planner output and elapsed time.
"""
def runPDDL(number):

    t2 = Process(target = waitw, args=())
    t2.start()

    manager = Manager()
    return_dict = manager.dict()
    t1 = Process(target = __starter2, args=(return_dict,number))
    t1.start()
    t1.join()
    t2.terminate()
    t1.terminate()

    t3 = Process(target = resw, args=(return_dict[0],return_dict[1]))
    t3.start()

#====================================================================================================

"""
    Run the execution that is chosen in the GUI, launching a different process.

    Return the output and elapsed time.
"""
def run(selected,number,n_rods):
    
    t2 = Process(target = waitw, args=())
    t2.start()

    manager = Manager()
    return_dict = manager.dict()
    t1 = Process(target = __starter, args=(return_dict, Execution.Color.colors, number, selected, n_rods))
    t1.start()
    t1.join()
    t2.terminate()
    t1.terminate()

    t3 = Process(target = resw, args=(return_dict[0],return_dict[1]))
    t3.start()

#====================================================================================================
"""
    Function that will be invoked when the
    button will be clicked in the main window
"""
def chooseColor():
    color = {}
    # variable to store hexadecimal code of color
    color['rgb'], color['hex'] = colorchooser.askcolor(title ="Choose color")
    Execution.Color.colors.append(str(color['hex']))

#====================================================================================================
"""
    Function that will be invoked when the
    button remove will be clicked in the main window.
    Removes the last color inside the list.
"""
def removeLastColor(x,y):
    try:
        Execution.Color.colors.pop()
    except Exception:
        t1 = Process(target = Message, args=(Message.INFO,"Note","The list of colors is empty",(x),(y)))
        t1.start()

#====================================================================================================

"""
    Returns a string containing all the color choosen.
"""
def visualizeColors():
    return "".join((str(color)+"\n" for color in Execution.Color.colors))

#====================================================================================================

"""
    Method that create a message for the user based on the number n that is choose.
"""
def searchInfo(n):

    if (n == 0):
        t1 = Process(target = Message, args=(Message.INFO,"Normal","Normal search with heuristic","","",3000))
    elif (n == 1):
        t1 = Process(target = Message, args=(Message.INFO,"Fast","Search with heuristic, but the problem is \npartitioned in 2 subproblem (MultiProcessing) \nwork only with 3 Rods","","",5000))
    elif (n == 2):
        t1 = Process(target = Message, args=(Message.INFO,"BFS","BFS, no Heuristic \n(It give optimum for the problem structure)\n Gives as solution only number of actions needed","","",5000))
    elif (n == 3):
        t1 = Process(target = Message, args=(Message.WARNING,"Fastest","Search with heuristic, but the problem is \npartitioned in 3 subproblem (MultiProcessing) \nwork only with 3 Rods","","",5000))
    elif (n == 4):
        t1 = Process(target = Message, args=(Message.WARNING,"Fastest Bfs","Search with BFS, but the problem is \npartitioned in 3 subproblem (MultiProcessing) \nwork only with 3 Rods","","",5000))
    else:
        t1 = Process(target = Message, args=(Message.ERROR,"Error","404"))

    t1.start()

#====================================================================================================
