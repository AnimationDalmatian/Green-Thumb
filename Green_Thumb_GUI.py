#

from tkinter import *

#constants
WIDTH = 800
HEIGHT = 500
FONTSIZE = 40

class MainGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg = "white")
        self.setupGUI()
    
    #configure GUI
    def setupGUI(self):
        self.display = Label(self, text = "", anchor = E, bg = "white", height = HEIGHT, width = WIDTH, font = ("", FONTSIZE))
        self.display.grid(row = 0, column = 0, columnspan = 4, sticky = E+W+N+S)
    
    #detect and respond to input from user on GUI
    def processInput(self, button):
        pass

######################  MAIN  ########################################
#create window
window = Tk()
window.title("Green Thumb")
#generate GUI
p = MainGUI(window)
#display and wait for user interaction
window.mainloop()
