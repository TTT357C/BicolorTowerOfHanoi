
import random
import colorsys
import sys
import time
from Zcanvas import *

sys.setrecursionlimit(10**6)

class ViewWindow:

    """
        This window is the moves viewer
    """

    def __init__(self):
        self.rootWindow = tk.Tk()
        self.done = False
        self.canvas = ZCanvas(self.rootWindow, width=1200, height=600, bg="white")
    class Piece:
        def __init__(self, canvas, width, value = 50, color = "#333333", border = True):
            self.width = width
            self.value = value
            self.height = width/3
            self.color = color
            self.border = border
            self.can = canvas

        def draw(self, i, j):

            x0_variation = self.value//2
            x1_variation = self.value-x0_variation

            try:
                if(self.border):
                    tu = tuple(int(str(self.color).replace("#","")[i:i+2], 16) for i in (0, 2, 4))

                    r, g, b = tu

                    h, l, s = colorsys.rgb_to_hls(r, g, b)

                    l = abs(l - 40)

                    r, g, b = colorsys.hls_to_rgb(h, l, s)

                    hexc = '#'+ '%02x%02x%02x' % (abs(int(r)), abs(int(g)), abs(int(b)))
                else:
                    hexc = self.color
            except Exception:
                hexc = self.color

            self.can.create_rectangle((j*self.width)+10+x0_variation, -(i*self.height+5), (j*self.width)+self.width-x1_variation, -((i*self.height)+self.height), width=2, outline = hexc, fill = self.color)

    def show_canvas(self):
        
        if(self.done == False):
            self.done = True
            tk.mainloop()
            


    #-----------------------------------------------------------------------


    def test1(self):

        global start_time
        start_time = time.time()

        p = []

        for i in range(10):
            p.append([])
            for j in range(10):
                p[i].append(self.Piece(self.canvas, 100, random.randint(1,100), self.random_color()))
                p[i][j].draw(i,j)
            print(i)


        print(f"--- {time.time() - start_time} seconds ---")

        self.show_canvas()

    def caller(self,s):
        self.canvas.delete("all")
        self.createFromTest(s)

    def dispose(self):
        self.rootWindow.destroy()

    def createFromTest(self, s):
        self.canvas.scalewidget.set(100)

        global start_time
        start_time = time.time()

        p = []

        max_ = -1
        for i in range(len(s.rods)):
            #stack = deepcopy(s.rods[i].getStack())
            stack = s.rods[i].getStack()
            for j in range(len(stack)):
                d = stack[j]
                if(d[0] > max_):
                    max_ = d[0]

        for i in range(len(s.rods)):
            p.append([])
            #stack = deepcopy(s.rods[i].getStack())
            #stack.reverse()
            
            stack = s.rods[i].getStack()
            
            for j in range(len(stack)):
                d = stack[j]
                #print(d.dimension)
                p[i].append(self.Piece(self.canvas, 100, 100-(d[0]*100/max_), d[1]))
                p[i][j].draw(j,i)
            #print(i)


        #print(f"--- {time.time() - start_time} seconds ---")

        self.show_canvas()

    def random_color():
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

if __name__ == "__main__":
    ViewWindow.test1()