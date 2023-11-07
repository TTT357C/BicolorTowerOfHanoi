
from ctypes import windll
from multiprocessing import Process
import sys

from tkinter import Spinbox, StringVar, Tk, Canvas, Button, PhotoImage
import MainWindowController as wc
from search.infomessage.Message import Message

sys.setrecursionlimit(10**6)

windll.shcore.SetProcessDpiAwareness(1) #For High DPI display

#====================================================================================================
"""
The MainWindow class represents the main window of the user interface. 

It handles:

- Initializing the Tk window and setting its size, position and background.
- Loading necessary images for buttons.
- Calling the initializer() method to draw all the GUI elements.
- Making the window non-resizable. 
- Starting the main window loop.

The initializer() method draws all the GUI elements:

- Creates a canvas covering the whole window.
- Draws rectangles, text and spinboxes for user data input 
  (number of disks, towers, etc).
- Draws rectangles and text for color selection.
- Displays the selected colors.
- Creates the button to start solution search.
- Creates the button to pick a new color. 
- Creates the button to remove the last picked color.

It basically handles drawing all the visual elements of the UI
inside the main window.

"""
#====================================================================================================

class MainWindow:

    
    #====================================================================================================
    """
    The __init__() method is the constructor for the MainWindow class. It handles:
    - Initializing the window dimensions (height and width)
    - Creating the Tk window object
    - Setting the gray background color
    - Calculating the centered position based on screen size
    - Setting the window size and position
    - Loading images for buttons 
    - Calling the initializer() method to draw the GUI
    - Making the window non-resizable 
    - Starting the main window loop

    """
    def __init__(self) -> None:
        self.height = 768
        self.width = 1024

        self.window = Tk()

        self.window.configure(bg = "#DCDCDC")
        w = 1024
        h = 768
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        #print(w, h, x, y)
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.image_image_1 = PhotoImage(file="search\\build0\\assets\\frame0\\image_1.png")
        self.button_image_1 = PhotoImage(file="search\\build0\\assets\\frame0\\button_1.png")
        self.button_image_2 = PhotoImage(file="search\\build0\\assets\\frame0\\button_2.png")
        self.button_image_3 = PhotoImage(file="search\\build0\\assets\\frame0\\button_3.png")
        self.button_image_4 = PhotoImage(file="search\\build0\\assets\\frame0\\button_4.png")
        self.button_image_5 = PhotoImage(file="search\\build0\\assets\\frame0\\button_5.png")

        self.initializer()

        self.window.resizable(False, False)
        self.window.mainloop()
    
    #====================================================================================================

    """
    The initializer() method draws all the GUI elements on the canvas:

    Parameters:
        self: The MainWindow object instance. 

    It handles:

    - Creating a canvas covering the whole window.
    - Drawing rectangles, text and spinboxes for user data input 
    (number of disks, towers, etc).
    - Drawing rectangles and text for color selection.
    - Displaying the selected colors.
    - Creating the button to start solution search.
    - Creating the button to pick a new color.
    - Creating the button to remove the last picked color.
    - Placing all the visual elements inside the canvas.

    It basically initializes and draws all the visual components 
    of the UI inside the main window.

    """

    def initializer(self):

        last_values=self.blank()

        canvas = Canvas(
        self.window,
        bg = "#FF792E",
        height = self.height,
        width = self.width,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
        434.0,
        0,
        1034.0,
        1065.0,
        fill="#FCFCFC",
        outline="")

        canvas.create_text(
        27.0,
        114.0,
        anchor="nw",
        text="Towers of Hanoi solver",
        fill="#FCFCFC",
        font=("", 26 * -1,"bold")
        )

        canvas.create_text(
        493.0,
        62,
        anchor="nw",
        text="Enter the needed data:",
        fill="#505485",
        font=("", 28 * -1,"bold")
        )

        canvas.create_text(
        493.0,
        131.0,
        anchor="nw",
        text="Number of Disks:",
        fill="#505485",
        font=("", 16 * -1,"bold")
        )

        canvas.create_text(
        493.0,
        167.0,
        anchor="nw",
        text="Number of Rods:",
        fill="#505485",
        font=("", 16 * -1,"bold")
        )


        self.s1=Spinbox(self.window, from_=2, to=9, width=7, textvariable = int(last_values[0].get()))
        self.s1.place(x=879.0, y=131.0, anchor='nw')
        self.s2=Spinbox(self.window, from_=3, to=9,width=7, textvariable = int(last_values[1].get()))
        self.s2.place(x=879.0, y=167.0, anchor='nw')
        self.s3=Spinbox(self.window, from_=0, to=4, width=7, textvariable = int(last_values[2].get()), command=self.changedSearch)
        self.s3.place(x=879.0, y=203.0, anchor='nw')

        canvas.create_rectangle(
        493.0,
        308.0,
        820.0,
        512.0,
        fill="#D9D9D9",
        outline="")

        canvas.create_text(
        493.0,
        203.0,
        anchor="nw",
        text="Choose Algorithm (Only search):",
        fill="#505485",
        font=("", 16 * -1,"bold")
        )

        canvas.create_text(
        495.0,
        272.0,
        anchor="nw",
        text="Color Choosen: (Only Search)",
        fill="#505485",
        font=("", 16 * -1,"bold")
        )

        canvas.create_text(
        502.0,
        317.0,
        anchor="nw",
        text = wc.visualizeColors(),
        fill="#505485",
        font=("", 16 * -1)
        )

        canvas.create_rectangle(
        27.0,
        160.0,
        87.0,
        165.0,
        fill="#FCFCFC",
        outline="")

        canvas.create_text(
        40.0,
        191.0,
        anchor="nw",
        text="Note: ",
        fill="#FCFCFC",
        font=("", 15 * -1,"bold")
        )

        canvas.create_text(
        40.0,
        217.0,
        anchor="nw",
        text="Made with Python",
        fill="#FCFCFC",
        font=("", 15 * -1)
        )

        canvas.create_text(
            40.0,
            275.0,
            anchor="nw",
            text="The speed of the solver depends on different factors, the main ones being the specifications of your PC and the current CPU usage.\n\nThe execution run as a different process for better efficiency. ",
            fill="#FCFCFC",
            font=("", 15 * -1),
            width=350
        )

        canvas.create_text(
        21.0,
        735.0,
        anchor="nw",
        text="By Thomas, Paolo e Mirko ",
        fill="#FCFCFC",
        font=("", 14 * -1)
        )

        image_1 = canvas.create_image(
            195.0,
            227.0,
            image=self.image_image_1
        )

        #PPDL
        
        button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonEventPDDLMultiProcessing,
            relief="flat"
        )
        button_1.place(
            x=493.0,
            y=680.0,
            width=456.0,
            height=55.0
        )

       
        
        button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command = self.buttonEventPDDL,
            relief="flat"
        )
        button_2.place(
            x=493.0,
            y=614.0,
            width=456.0,
            height=55.0
        )

        #Color
        
        button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command = self.buttonEventColor,
            relief="flat"
        )
        button_3.place(
            x=827.0,
            y=308.0,
            width=124.0,
            height=131.0
        )

        #Search
        
        button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command = self.buttonEventSearch,
            relief="flat"
        )
        button_4.place(
            x=493.0,
            y=549.0,
            width=456.0,
            height=55.0
        )

        button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command = self.buttonRemove,
            relief="flat"
        )
        button_5.place(
            x=827.0,
            y=446.0,
            width=124.0,
            height=66.0
        )
    
    
    #====================================================================================================

    """
    The blank() method clears all widgets from the main window canvas.

    Parameters:
    self: The MainWindow object instance.

    It loops through all the widgets currently on the canvas 
    and destroys/deletes them to clear the canvas.

    This allows redrawing the canvas with new widgets as needed.
    """
    def blank(self):

        s1_var = StringVar(self.window)
        s2_var = StringVar(self.window)
        s3_var = StringVar(self.window)
        try:
            s1_var.set(str(self.s1.get()))
            s2_var.set(str(self.s2.get()))
            s3_var.set(str(self.s3.get()))
        except Exception:
            s1_var.set("0")
            s2_var.set("1")
            s3_var.set("2")

        #clear
        for widgets in self.window.winfo_children():
            widgets.destroy()

        return [s1_var,s2_var,s3_var]
    
    
    #====================================================================================================

    """
    The buttonEventColor() method is called when the "Pick Color" button is clicked.

    It handles:

    - Withdrawing the main window temporarily.
    - Clearing the canvas by calling blank().
    - Calling chooseColor() to open the color picker dialog.
    - Re-drawing the GUI by calling initializer().
    - Restoring the main window.

    This allows the user to pick a new color, which will get 
    added to the color list and displayed in the GUI when
    it is re-drawn.

    Parameters:
    self: The MainWindow object instance.
    """

    def buttonEventColor(self):
        self.window.withdraw()
        self.blank()
        wc.chooseColor()
        self.initializer()
        self.window.deiconify()

    #====================================================================================================

    """
    The buttonEventSearch() method is called when the "Search Solution" button is clicked. 

    It handles:

    - Withdrawing the main window temporarily.
    - Clearing the canvas by calling blank().
    - Updating the window.
    - Calling the run() method to start the solution search process in background.
    - Re-drawing the GUI by calling initializer(). 
    - Restoring the main window.

    This allows starting the solution search process without blocking the UI.

    It first checks if at least 2 colors have been selected. If not, it 
    displays an error message at the center of the screen.

    Parameters:
    self: The MainWindow object instance.
    """

    def buttonEventSearch(self):
        
        if (len(wc.Execution.Color.colors)>=2):
            i1=int(self.s3.get())
            i2=int(self.s1.get())
            i3=int(self.s2.get())

            #Check Minimum
            i2 = max(i2, 2)
            i3 = max(i3, 3)
 
            if i3 == 3 or i1 in [0,2]:
                self.window.withdraw()
                self.blank()
                self.window.update()
                wc.run(i1,i2,i3)
                self.initializer()
                self.window.deiconify()
            else:
                t1 = Process(target = Message, args=(Message.ERROR,"Error","This method of search doesn't work \nwith more than 3 rods",(self.window.winfo_x()+self.width/2),(self.window.winfo_y()+self.height/2)))
                t1.start()
        else:
            t1 = Process(target = Message, args=(Message.ERROR,"Error","The color you have chosen aren't enough",(self.window.winfo_x()+self.width/2),(self.window.winfo_y()+self.height/2)))
            t1.start()

    #====================================================================================================

    """
    The buttonEventPDDL() method is called when the "PDDL" button is clicked.
    
    It handles:
    
    - Getting the disk number from self.s1 Spinbox
    - Getting the rod number from self.s2 Spinbox 
    - Checking that disk and rod numbers are valid:
        - Disk number must be >= 2
        - Rod number must be >= 3
    - Withdrawing the main window 
    - Calling blank() to show a blank window 
    - Updating the main window
    - Calling wc.runPDDL() to execute the PDDL search
    - Calling initializer() to re-initialize the main window
    - Deiconifying the main window to show it again
    """
    def buttonEventPDDL(self):

        i2=int(self.s1.get())
        i3=int(self.s2.get())

        #Check Minimum
        i2 = max(i2, 2)
        i3 = max(i3, 3)

        self.window.withdraw()
        self.blank()
        self.window.update()
        wc.runPDDL(i2,i3)
        self.initializer()
        self.window.deiconify()

    #====================================================================================================

    """
    The buttonEventPDDLMultiProcessing() method is called when the "PDDL MultiProcessing" button is clicked.

    It handles:

    - Getting the number of disks and rods entered by the user from the Spinbox widgets.
    - Validating that the number of disks is between 4-6 and rods is 3, otherwise showing an error.
    - Withdrawing and blanking the main window, updating it, and running the PDDL multi-processing 
    search using the wc.runPDDLMulti() method from MainWindowController.
    - Restoring the main window and redrawing the GUI with initializer().

    This allows the user to run a multi-processing PDDL search on valid disk/rod combinations.
    The results will be shown in a new window.

    Parameters:
    self: The MainWindow object instance.
    """
    def buttonEventPDDLMultiProcessing(self):

        i2=int(self.s1.get())
        i3=int(self.s2.get())

        #Check Minimum
        i2 = max(i2, 2)
        i3 = max(i3, 3)

        if i3 == 3 and i2 in [4,5,6]:
            self.window.withdraw()
            self.blank()
            self.window.update()
            wc.runPDDLMulti(i2)
            self.initializer()
            self.window.deiconify()
        else:
            t1 = Process(target = Message, args=(Message.ERROR,"Error","Disk number [4 - 6] or rod one not supported (3)",(self.window.winfo_x()+self.width/2),(self.window.winfo_y()+self.height/2)))
            t1.start()
        
    #====================================================================================================
    """
    The buttonRemove() method is called when the "Remove Color" button is clicked.

    It handles:

    - Calling the removeLastColor() method in MainWindowController 
    to remove the last color from the color list.

    - Passing the x and y position of the main window 
    so error popups can be positioned correctly.

    - Calling initializer() to redraw the GUI with the updated
    color list.

    This allows the user to remove the last picked color, which 
    will be reflected in the GUI when it is redrawn.

    Parameters:
    self: The MainWindow object instance.
    """
    def buttonRemove(self):
        wc.removeLastColor((self.window.winfo_x()),(self.window.winfo_y()))
        self.blank()
        self.window.update()
        self.initializer()

    #====================================================================================================

    """
    Handles the event when the search algorithm is changed.

    Calls the searchInfo method from the MainWindowController module, 
    passing the selected index of the search algorithm, to 
    display an informational message about the selected algorithm.

    Parameters:
    self: The MainWindow object instance.
    """
    def changedSearch(self):
        print(self.s3.get())
        wc.searchInfo(int(self.s3.get()))

#====================================================================================================

#Main
if __name__ == "__main__":
    MainWindow()

#====================================================================================================