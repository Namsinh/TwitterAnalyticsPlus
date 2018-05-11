from tkinter import *
from tkinter.scrolledtext import ScrolledText
import analyzer

def init():
    #Main Window
    global window
    window = Tk()
    window.title('Twitter Analytics+')
    window.geometry("250x350")
    createWidgets()
    positionWidgets()
    configureWidgets()
    window.mainloop()

def createWidgets():
    global column; column = Frame(window)
    global welcomeLabel; welcomeLabel = Label(window)
    global getClassificationButt; getClassificationButt = Button(window)

def positionWidgets():

    column.place(relx=.5, rely=.5, anchor=CENTER)
    welcomeLabel.pack(in_=column, side=TOP)
    getClassificationButt.pack(in_=column, side=BOTTOM, pady=10, fill="both")

def configureWidgets():
    window.configure(background="wheat2")
    column.configure(background="wheat2")
    
    welcomeTxt= "Welcome to Twitter Analytics+\n\n This tool has been developed\n to bring awareness on the content \nwe consume on Social Media."
    welcomeLabel.configure(width=300, height=10, text=welcomeTxt, relief=FLAT)
    getClassificationButt.configure(text="Let's get started!", background="wheat2", height=2, width=20, command=startAction)

def startAction():
    inWindow = Toplevel()
    inWindow.geometry("600x350")
    inWindow.title('Sentiment & Classification Report')
    inWindow.configure(background="wheat2")

    global usernameEntry
    global classDisplay

    innerFrame = Frame(inWindow)
    outterFrame = Frame(inWindow)

    usernameLabel = Label(inWindow)
    usernameEntry = Entry(inWindow)
    
    classButton = Button(inWindow)
    classDisplay = ScrolledText(inWindow)
    
    usernameLabel.pack(in_=innerFrame, side=LEFT)
    usernameEntry.pack(in_=innerFrame, side=RIGHT)

    innerFrame.pack(in_=outterFrame, side=TOP)
    classDisplay.pack(in_=outterFrame, side=BOTTOM)
    classButton.pack(in_=outterFrame, side=BOTTOM)
    
    outterFrame.grid(column=0, row=0, padx=3, pady=3)

    outterFrame.configure(background="wheat2")
    innerFrame.configure(pady=4, background="wheat2")
    classButton.configure(width=10, height=1, background="wheat2", text="Get Insight", pady=3, padx=1, command=getClassAction)     #Configures widgets
    usernameLabel.configure(width=10, height=1, text="Username @", relief=FLAT, background="wheat2")
    classDisplay.configure(height=17, pady=5, padx=5, border=1, relief="groove")

    
def getClassAction():
    usernameInput = str(usernameEntry.get())
    reportTxt = "Here's an overview on @" + usernameInput + ":\n"
    classDisplay.insert(INSERT, reportTxt)

    tUser = analyzer.analyze(usernameInput)

    classDisplay.insert(END, tUser)
