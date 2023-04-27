from tkinter import *
from matplotlib import *
from Draw_Graph import *

#constants
WIDTH = 800
HEIGHT = 800
FONTSIZE = 30

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
        global widgetList, graph
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
        
        #Set up table                                   #use same data from graph for table
        optionsText = ""
        resultsText = ""
        for i in data:
            optionsText += (str(i) + "\n")
            resultsText += (str(data[i]) + "\n")
        
        self.optionsList = Label(text = optionsText, font = ("", FONTSIZE), borderwidth = 2, relief = "ridge", justify = LEFT, width = 9)    #add borders
        self.resultsList = Label(text = resultsText, font = ("", FONTSIZE), borderwidth = 2, relief = "ridge", justify = RIGHT)    #add borders
        
        self.optionsList.grid(row = 1, sticky = W)
        self.resultsList.grid(row = 1, sticky = E)
        widgetList = [self.backButton, self.optionsList, self.resultsList]
    
    #Changes screen to display water schedule screen
    def waterScheduleScreen(self):
        global widgetList
        self.clearWindow()
        img1 = PhotoImage(file="Graphics/BackButton.gif")
        self.backButton = Button(self.parent, image = img1, anchor = N+E, command = self.homeScreen)
        self.backButton.grid()
        self.backButton.image = img1
        self.watered = Label(text = "\n\n\nYour last watering was...\nYour next scheduled watering is...\n\n\n", font = ("", FONTSIZE))      #Can be connected to last recorded data?
        self.watered.grid()
        widgetList = [self.backButton, self.watered]
    
    #Changes screen to display settings menu
    def settingsScreen(self):
        global widgetList
        self.clearWindow()
        img1 = PhotoImage(file="Graphics/BackButton.gif")
        self.backButton = Button(self.parent, image = img1, anchor = N+E, command = self.homeScreen)
        self.backButton.grid()
        self.backButton.image = img1
        settingsDisclaimer = "\n\n\nDue to time constraints, customization for\nthe plant's voice, GUI theme, and other settings were cut.\nSorry about that!\n\n\n"
        self.settingsText = Label(text = settingsDisclaimer, font = ("", FONTSIZE))
        self.settingsText.grid()
        widgetList = [self.backButton, self.settingsText]

#################################  MAIN  ########################################
#create window
window = Tk()
window.title("Green Thumb")
#generate GUI
p = MainGUI(window)
#display and wait for user interaction
window.mainloop()
