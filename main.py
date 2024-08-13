from tkinter import *
import csv

# App config
app = Tk()
app.geometry('450x450')
app.title('Mode')

# Widgets
mainFrame = Frame(app)
mainFrame.pack()

welcomeLabel = Label(mainFrame, text='Welcome to Mode!', font=('Arial', 35))
welcomeLabel.pack()

controlFrame = Frame(mainFrame)
controlFrame.pack()


app.mainloop()
