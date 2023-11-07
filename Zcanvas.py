
# An extended Python/tkinter Canvas Window with zoom scale and extended bindings
# on which we can draw points, lines, rectangles, etc.
# See the Python tkinter module, Canvas class, for more usage details
# A modified implementation of https://github.com/samyzaf/xcanvas

import tkinter as tk

class ZCanvas(tk.Canvas):
    def __init__(self, rootwin, **opt):
        width = opt.get("width", 1000)
        height = opt.get("height", 600)
        bg = opt.get("bg", "white")
        scrollbars = opt.get("scrollbars", True)
        scalewidget = opt.get("scalewidget", True)
        x_axis = opt.get("x_axis", 7)
        y_axis = opt.get("y_axis", 7)

        self.region = (0, -height, width, 0)
        self.rootwin = rootwin
        self.rootframe = tk.Frame(rootwin, width=width, height=height, bg=bg)
        self.rootframe.pack(expand=True, fill=tk.BOTH)
        tk.Canvas.__init__(self, self.rootframe, width=width, height=height, bg=bg, scrollregion=self.region)
        self.config(highlightthickness=0)

        if scrollbars:
            self.scrollbars()

        self.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    
        self.scalewidget = tk.Scale(self.rootframe, from_=10, to=400, length=500,
                                    orient=tk.VERTICAL, font="Consolas 6", command=self.resize)
        self.scalewidget.set(100)
        if scalewidget:
            self.scalewidget.pack(side=tk.LEFT, fill=tk.Y, expand=False)
        else:
            self.scalewidget.place(x=100000, y=100000)

        self.xview_moveto(0)
        self.yview_moveto(0)
        if x_axis or y_axis:
            self.draw_axis(x_axis, y_axis)
        self.bindings()

    def scrollbars(self):
        self.sbarV = tk.Scrollbar(self.rootframe, orient = tk.VERTICAL)
        self.sbarH = tk.Scrollbar(self.rootframe, orient = tk.HORIZONTAL)
        self.sbarV.config(command = self.yview)
        self.sbarH.config(command = self.xview)
        self.config(yscrollcommand = self.sbarV.set)
        self.config(xscrollcommand = self.sbarH.set)
        self.sbarV.pack(side = tk.RIGHT, fill = tk.Y)
        self.sbarH.pack(side = tk.BOTTOM, fill = tk.X)
    
    def bindings(self):
        self.bind("<Control-MouseWheel>", self.onCtrlMouseWheel)
        self.bind("<Alt-MouseWheel>", self.onAltMouseWheel)
        self.bind("<MouseWheel>", self.onMouseWheel)
        self.bind("<Shift-MouseWheel>", self.onShiftMouseWheel)
        self.bind("f", self.fit_canvas)
        self.bind("<Home>", self.fit_canvas)
        self.bind("<Up>", self.onArrowUp)
        self.bind("<Down>", self.onArrowDown)
        self.bind("<Left>", self.onArrowLeft)
        self.bind("<Right>", self.onArrowRight)
        self.bind("<Prior>", self.onArrowUp)
        self.bind("<Next>", self.onArrowDown)
        self.bind("<Shift-Prior>", self.onPrior)
        self.bind("<Shift-Next>", self.onNext)

    def show(self, force=False):
        if force or not self.winfo_ismapped():
            self.rootwin.iconify()
            self.rootwin.update()
            self.rootwin.deiconify()
            self.rootwin.lift()

    def hide(self):
        self.rootwin.iconify()

    def resize(self, percent):
        x1,y1,x2,y2 = self.region
        canvas_breadth = max(x2-x1, y2-y1)
        _region = self.config('scrollregion')[4].split()
        region = tuple(float(x) for x in _region)
        x1,y1,x2,y2 = region
        breadth = max(x2-x1, y2-y1)
        if breadth == 0:
            return
        r = float(percent) / 100
        if r < 0.01 or r > 30:
            return
        s = r / (float(breadth) / canvas_breadth)
        self.scale('all', 0, 0, s, s)
        nregion = tuple(x*r for x in self.region)
        self.config(scrollregion=nregion)

    def onCtrlMouseWheel(self, event):
        s = self.scalewidget.get()
        if event.delta > 0:
            s += 15
        else:
            s -= 15
        self.scalewidget.set(s)
    
    def onAltMouseWheel(self, event):
        s = self.scalewidget.get()
        if event.delta > 0:
            s += 5
        else:
            s -= 5
        self.scalewidget.set(s)
    
    def onMouseWheel(self, event):
        self.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def onArrowUp(self, event):
        if event.keysym == "Up":
            self.yview_scroll(-1, "units")
        else:
            self.yview_scroll(-1, "pages")
    
    def onArrowDown(self, event):
        if event.keysym == "Down":
            self.yview_scroll(1, "units")
        else:
            self.yview_scroll(1, "pages")
    
    def onArrowLeft(self, event):
        self.xview_scroll(-1, "units")
    
    def onArrowRight(self, event):
        self.xview_scroll(1, "units")
    
    def onPrior(self, event):
        self.xview_scroll(1, "pages")
    
    def onNext(self, event):
        self.xview_scroll(-1, "pages")
    
    def onShiftMouseWheel(self, event):
        self.xview_scroll(int(-1*(event.delta/120)), "units")
    
    def fit_canvas(self, event):
        print(event.keysym)
        self.scalewidget.set(100)
    
    def draw_axis(self, m, n):
        pass

    def eventEcho(self, event):
        print(event.keysym)

