#Subfile which will draw graph for top right button's screen. 
#This will be imported to the main file and used in a widget.
from matplotlib import *
from tkinter import *
import Moisture_Sensor as mS
#TkAgg is made to integrate with Tkinter
use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter Matplotlib Demo')
        
        #600x400 pixels
        self.figure = Figure(figsize=(6,4), dpi=100)
        self.figure_canvas = FigureCanvasTkAgg(self.figure, self)
        NavigationToolbar2Tk(self.figure_canvas, self)

        #Establish axes for graph
        data = {k:v for (k,v) in zip(mS.times, mS.moistures)}
        options = data.keys()
        results = data.values()
        
        axes = self.figure.add_subplot()
        axes.plot(options, results)
        axes.set_title("Water Over Time")
        axes.set_ylabel("Water Level")
        axes.set_xlabel("Time")
        self.figure_canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        
