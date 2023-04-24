#To add:
##Make graphics high quality
##Creating Screens 2-5
##Saving information to a file so that it can be accessed even when the program closes
from tkinter import *
from matplotlib import *
from Draw_Graph import *

#constants
WIDTH = 800
HEIGHT = 800
FONTSIZE = 40

#initialize widget list which will later be filled with widgets that are
#on screen, in order for them to be destroyed when a button is pressed
widgetList = []

class MainGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg = "white")
        self.parent = parent
        self.setupGUI()
        self.homeScreen()
    
    #Clear everything in window
    def clearWindow(self):
        global widgetList
        for widget in widgetList:
            try:
                widget.destroy()
            except:
                pass
    
    #configure GUI
    def setupGUI(self):
        self.display = Label(self, text = "", anchor = E, bg = "white", height = HEIGHT, width = WIDTH, font = ("", FONTSIZE))
    
    #Changes screen to display home screen
    def homeScreen(self):
        global widgetList
        #top left button
        self.clearWindow()
        img1 = PhotoImage(file="Graphics/HomeButton1.gif")
        self.homeButton1 = Button(self.parent, image=img1, command = self.waterOverTimeScreen)
        self.homeButton1.grid(row=0, column=0, sticky=N+S+E+W)
        self.homeButton1.image = img1
        #top right button
        img2 = PhotoImage(file="Graphics/HomeButton2.gif")
        self.homeButton2 = Button(self.parent, image=img2, command = self.sensorFeedbackScreen)
        self.homeButton2.grid(row=0, column=1, sticky=N+S+E+W)
        self.homeButton2.image = img2
        #bottom left button
        img3 = PhotoImage(file="Graphics/HomeButton3.gif")
        self.homeButton3 = Button(self.parent, image=img3, command = self.waterScheduleScreen)
        self.homeButton3.grid(row=1, column=0, sticky=N+S+E+W)
        self.homeButton3.image = img3
        #bottom right button
        img4 = PhotoImage(file="Graphics/HomeButton4.gif")
        self.homeButton4 = Button(self.parent, image=img4, command = self.settingsScreen)
        self.homeButton4.grid(row=1, column=1, sticky=N+S+E+W)
        self.homeButton4.image = img4
        widgetList = [self.homeButton1, self.homeButton2, self.homeButton3, self.homeButton4]
        
    #Changes screen to display water over time graph
    def waterOverTimeScreen(self):
        global widgetList
        self.clearWindow()
        img1 = PhotoImage(file="Graphics/BackButton.gif")
        self.backButton = Button(self.parent, image = img1, anchor = N+E, command = self.homeScreen)
        self.backButton.grid()
        self.backButton.image = img1
        #Create chart from Draw_Graph.py
        self.app = App()
        widgetList = [self.backButton, self.app]
    
    #Changes screen to display real-time sensor feedback screen
    def sensorFeedbackScreen(self):
        global widgetList
        self.clearWindow()
        img1 = PhotoImage(file="Graphics/BackButton.gif")
        self.backButton = Button(self.parent, image = img1, anchor = N+E, command = self.homeScreen)
        self.backButton.grid()
        self.backButton.image = img1
        widgetList = [self.backButton]
    
    #Changes screen to display water schedule screen
    def waterScheduleScreen(self):
        global widgetList
        self.clearWindow()
        img1 = PhotoImage(file="Graphics/BackButton.gif")
        self.backButton = Button(self.parent, image = img1, anchor = N+E, command = self.homeScreen)
        self.backButton.grid()
        self.backButton.image = img1
        widgetList = [self.backButton]
    
    #Changes screen to display settings menu
    def settingsScreen(self):
        global widgetList
        self.clearWindow()
        img1 = PhotoImage(file="Graphics/BackButton.gif")
        self.backButton = Button(self.parent, image = img1, anchor = N+E, command = self.homeScreen)
        self.backButton.grid()
        self.backButton.image = img1
        widgetList = [self.backButton]

#################################  MAIN  ########################################
#create window
window = Tk()
window.title("Green Thumb")
#generate GUI
p = MainGUI(window)
#display and wait for user interaction
window.mainloop()
