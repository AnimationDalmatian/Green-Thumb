#To add:
##Make graphics high quality
##Creating Screens 2-5
##Saving information to a file so that it can be accessed even when the program closes

from tkinter import *

#constants
WIDTH = 800
HEIGHT = 800
FONTSIZE = 40

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
            widget.destroy()
    
    #configure GUI
    def setupGUI(self):
        self.display = Label(self, text = "", anchor = E, bg = "white", height = HEIGHT, width = WIDTH, font = ("", FONTSIZE))
        #self.display.grid(row = 0, column = 0, columnspan = 4, sticky = E+W+N+S)
    
    #Changes screen to display home screen
    def homeScreen(self):
        global widgetList
        #top left button
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
        self.backButton = Button(self.parent, text = "waterOverTime", anchor = N, height = 20, width = 150, command = self.homeScreen)
        self.backButton.pack()
        widgetList = [self.backButton]
    
    #Changes screen to display real-time sensor feedback screen
    def sensorFeedbackScreen(self):
        global widgetList
        self.clearWindow()
        self.backButton = Button(self.parent, text = "sensorFeedback", anchor = N, height = 20, width = 150, command = self.homeScreen)
        self.backButton.pack()
        widgetList = [self.backButton]
    
    #Changes screen to display water schedule screen
    def waterScheduleScreen(self):
        global widgetList
        self.clearWindow()
        self.backButton = Button(self.parent, text = "waterSchedule", anchor = N, height = 20, width = 150, command = self.homeScreen)
        self.backButton.pack()
        widgetList = [self.backButton]
    
    #Changes screen to display settings menu
    def settingsScreen(self):
        global widgetList
        self.clearWindow()
        self.backButton = Button(self.parent, text = "settings", anchor = N, height = 20, width = 150, command = self.homeScreen)
        self.backButton.pack()
        widgetList = [self.backButton]

#################################  MAIN  ########################################
#create window
window = Tk()
window.title("Green Thumb")
#generate GUI
p = MainGUI(window)
#display and wait for user interaction
window.mainloop()
