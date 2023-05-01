from tkinter import *
from matplotlib import *
from Draw_Graph import *
import Moisture_Sensor as mS

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
                self.app.destroy()
    
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
        img2 = PhotoImage(file="Graphics/UpdateButton.gif")
        self.backButton = Button(self.parent, image = img1, anchor = N+E, command = self.homeScreen)
        self.updateButton = Button(self.parent, image = img2, anchor = N+W, command = self.updateGraph)
        self.status = Label(text = "", font = ("", FONTSIZE), borderwidth = 2, relief = "ridge")
        self.backButton.grid(row = 0, column = 0)
        self.updateButton.grid(row = 0, column = 1)
        self.status.grid(row = 1, columnspan = 2)
        self.backButton.image = img1
        self.updateButton.image = img2
        #Create chart from Draw_Graph.py
        self.app = App()
        widgetList = [self.backButton, self.app, self.updateButton, self.status]
    
    #Changes screen to display real-time sensor feedback screen
    def sensorFeedbackScreen(self):
        global widgetList
        self.clearWindow()
        img1 = PhotoImage(file="Graphics/BackButton.gif")
        img2 = PhotoImage(file="Graphics/UpdateButton.gif")
        self.backButton = Button(self.parent, image = img1, anchor = N+E, command = self.homeScreen)
        self.updateButton = Button(self.parent, image = img2, anchor = N+W, command = self.updateChart)
        self.status = Label(text = "", font = ("", FONTSIZE), borderwidth = 2, relief = "ridge")
        self.backButton.image = img1
        self.updateButton.image = img2
        self.backButton.grid(row = 0, column = 0)
        self.updateButton.grid(row = 0, column = 1)
        self.status.grid(row = 1, columnspan = 2)
        
        self.timeList = Label(text = "", font = ("", FONTSIZE), borderwidth = 2, relief = "ridge", justify = LEFT)
        self.moistureList = Label(text = "", font = ("", FONTSIZE), borderwidth = 2, relief = "ridge", justify = RIGHT)
        self.timeList.grid(row = 1, sticky = W)
        self.moistureList.grid(row = 1, sticky = E)
        #Set up table                                   #use same data from graph for table 
        self.updateChart()
        widgetList = [self.backButton, self.updateButton, self.timeList, self.moistureList]
        
    #Changes screen to display water schedule screen
    def waterScheduleScreen(self):
        global widgetList
        self.clearWindow()
        img1 = PhotoImage(file="Graphics/BackButton.gif")
        self.backButton = Button(self.parent, image = img1, anchor = N+E, command = self.homeScreen)
        self.watered = Label(text = "\n\n\nEnter your next planned watering...:\n\n\n", font = ("", FONTSIZE))
        self.textBox = Text(self.parent, height = 3)
        
        self.backButton.grid(row = 0)
        self.watered.grid(row = 1)
        self.textBox.grid(row = 2)
        self.backButton.image = img1
        
        widgetList = [self.backButton, self.watered, self.textBox]
    
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

    def updateGraph(self):
        global widgetList
        mS.readSensor()
        self.app.destroy()
        self.status.destroy()
        self.app = App()
        
        #determine whether or not the plant has enough water
        statusText = 0
        for num in mS.moistures:
            statusText += num
        statusText /= len(mS.moistures)
        if(statusText < 800):
            statusText = "The plant needs water!"
        else:
            statusText = "The plant has enough water!"
        
        self.status = Label(text = statusText, font = ("", FONTSIZE), borderwidth = 2, relief = "ridge")
        self.status.grid(row = 1, columnspan = 2)
        
        widgetList = [self.backButton, self.updateButton, self.app, self.status]
        
        
    def updateChart(self):
        global widgetList
        self.moistureList.destroy()
        self.timeList.destroy()
        self.status.destroy()
        mS.readSensor()
        self.moistureText = "Readings:\n"
        self.timeText = "Time:\n"
        for i in mS.moistures:
            self.moistureText += (str(i) + "\n")
            
        for i in mS.times:
            self.timeText += (str(i) + "\n")
        
        #determine whether or not the plant has enough water
        statusText = 0
        for num in mS.moistures:
            statusText += num
        statusText /= len(mS.moistures)
        if(statusText < 800):
            statusText = "The plant needs water!"
        else:
            statusText = "The plant has enough water!"
        
        self.timeList = Label(text = self.timeText, font = ("", FONTSIZE), borderwidth = 2, relief = "ridge", justify = LEFT)
        self.moistureList = Label(text = self.moistureText, font = ("", FONTSIZE), borderwidth = 2, relief = "ridge", justify = RIGHT)
        self.status = Label(text = statusText, font = ("", FONTSIZE), borderwidth = 2, relief = "ridge")
        self.timeList.grid(row = 1, column = 0, columnspan = 2)
        self.moistureList.grid(row = 1, column = 2, columnspan = 2)
        self.status.grid(row = 2, columnspan = 4)
        
        widgetList = [self.backButton, self.updateButton, self.timeList, self.moistureList, self.status]

#################################  MAIN  ########################################
#create window
window = Tk()
window.title("Green Thumb")
#generate GUI
p = MainGUI(window)
#display and wait for user interaction
window.mainloop()
