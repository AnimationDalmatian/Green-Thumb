#Subfile which will draw graph for top right button's screen. 
#This will be imported to the main file and used in a widget.
#To use matplotlib - pip install matplotlib
from matplotlib import *
from tkinter import *
import Green_Thumb_MoistureSensor as mS
#TkAgg is made to integrate with Tkinter
use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter Matplotlib Demo')
        #set data
        data = {
            'OptionA': 1,
            'OptionB': 3,
            'OptionC': 2
        }
        options = data.keys()
        results = data.values()

        #600x400 pixels
        figure = Figure(figsize=(6,4), dpi=100)
        figure_canvas = FigureCanvasTkAgg(figure, self)
        NavigationToolbar2Tk(figure_canvas, self)

        #Establish axes for graph
        axes = figure.add_subplot()
        axes.plot(options, results)
        axes.set_title("Test")
        axes.set_ylabel("Options")
        figure_canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)