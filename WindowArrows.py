import sys
import tkinter as tk
import tkinter.font as tkFont

from ViewWindow import ViewWindow

sys.setrecursionlimit(10**6)

class WindowArrows:

    """
        This window change the move that is diplayed on ViewWindow
    """
    def __init__(self, result, n):

        root = tk.Tk()
        self.n = n
        self.b = 0
        #setting title
        root.title("Controller")
        #setting window size
        width=320
        height=80
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.result=result

        GButton_Left=tk.Button(root)
        GButton_Left["activebackground"] = "#ffffff"
        GButton_Left["bg"] = "#fcfcfc"
        GButton_Left["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=33)
        GButton_Left["font"] = ft
        GButton_Left["fg"] = "#000000"
        GButton_Left["justify"] = "center"
        GButton_Left["text"] = "⏮"
        GButton_Left.place(x=0,y=0,width=80,height=80)
        GButton_Left["command"] = self.GButton_FLeft_command

        GButton_Right=tk.Button(root)
        GButton_Right["activebackground"] = "#ffffff"
        GButton_Right["bg"] = "#fcfcfc"
        ft = tkFont.Font(family='Times',size=33)
        GButton_Right["font"] = ft
        GButton_Right["fg"] = "#000000"
        GButton_Right["justify"] = "center"
        GButton_Right["text"] = "◀"
        GButton_Right.place(x=80,y=0,width=80,height=80)
        GButton_Right["command"] = self.GButton_Left_command

        GButton_Left=tk.Button(root)
        GButton_Left["activebackground"] = "#ffffff"
        GButton_Left["bg"] = "#fcfcfc"
        GButton_Left["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=33)
        GButton_Left["font"] = ft
        GButton_Left["fg"] = "#000000"
        GButton_Left["justify"] = "center"
        GButton_Left["text"] = "▶"
        GButton_Left.place(x=160,y=0,width=80,height=80)
        GButton_Left["command"] = self.GButton_Right_command

        GButton_Left=tk.Button(root)
        GButton_Left["activebackground"] = "#ffffff"
        GButton_Left["bg"] = "#fcfcfc"
        GButton_Left["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=33)
        GButton_Left["font"] = ft
        GButton_Left["fg"] = "#000000"
        GButton_Left["justify"] = "center"
        GButton_Left["text"] = "⏭"
        GButton_Left.place(x=240,y=0,width=80,height=80)
        GButton_Left["command"] = self.GButton_FRight_command

        node=self.result[self.n]

        self.v = ViewWindow()
        self.v.caller(node.state)

        root.mainloop()

    def GButton_Left_command(self):
        if(self.n <= 0):
            pass
        else:
            self.n-=1
            n=self.result[self.n]
            self.v.caller(n.state)

    def GButton_FLeft_command(self):
        if(self.n <= 5):
            pass
        else:
            self.n-=5
            n=self.result[self.n]
            self.v.caller(n.state)

    def GButton_Right_command(self):
        if(self.n < len(self.result)-1):
            self.n+=1
            n=self.result[self.n]
            self.v.caller(n.state)
            

    def GButton_FRight_command(self):
        if(self.n < len(self.result)-6):
            self.n+=5
            n=self.result[self.n]
            self.v.caller(n.state)
