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
        self.setupGUI()
        self.homeScreen(parent)
    
    #configure GUI
    def setupGUI(self):
        self.display = Label(self, text = "", anchor = E, bg = "white", height = HEIGHT, width = WIDTH, font = ("", FONTSIZE))
        #self.display.grid(row = 0, column = 0, columnspan = 4, sticky = E+W+N+S)
    
    #Remove home screen buttons
    def clearFrame(self):
        for widget in window.winfo_children():
            widget.destroy()
    
    #Changes screen to display home screen
    def homeScreen(self, parent):
        self.clearFrame()
        #top left button
        img1 = PhotoImage(file="Graphics/HomeButton1.gif")
        self.homeButton1 = Button(parent, image=img1, command = self.waterOverTimeScreen)
        self.homeButton1.grid(row=0, column=0, sticky=N+S+E+W)
        self.homeButton1.image = img1
        #top right button
        img2 = PhotoImage(file="Graphics/HomeButton2.gif")
        self.homeButton2 = Button(parent, image=img2, command = self.sensorFeedbackScreen)
        self.homeButton2.grid(row=0, column=1, sticky=N+S+E+W)
        self.homeButton2.image = img2
        #bottom left button
        img3 = PhotoImage(file="Graphics/HomeButton3.gif")
        self.homeButton3 = Button(parent, image=img3, command = self.waterScheduleScreen)
        self.homeButton3.grid(row=1, column=0, sticky=N+S+E+W)
        self.homeButton3.image = img3
        #bottom right button
        img4 = PhotoImage(file="Graphics/HomeButton4.gif")
        self.homeButton4 = Button(parent, image=img4, command = self.settingsScreen)
        self.homeButton4.grid(row=1, column=1, sticky=N+S+E+W)
        self.homeButton4.image = img4
        
    #Changes screen to display water over time graph
    def waterOverTimeScreen(self):
        self.clearFrame()
        self.backButton = Button(self, text = "BACK", anchor = N, height = 20, width = 150, command = self.homeScreen)
        self.backButton.pack
    
    #Changes screen to display real-time sensor feedback screen
    def sensorFeedbackScreen(self):
        pass
        # self.homeScreenDel()
    
    #Changes screen to display water schedule screen
    def waterScheduleScreen(self):
        pass
        # self.homeScreenDel()
    
    #Changes screen to display settings menu
    def settingsScreen(self):
        pass
        # self.homeScreenDel()
    
    #detect and respond to input from user on GUI
    # def processInput(self, button):
        # pass

#################################  MAIN  ########################################
#create window
window = Tk()
window.title("Green Thumb")
#generate GUI
p = MainGUI(window)
#display and wait for user interaction
window.mainloop()
