from tkinter import *
from tkinter import filedialog
import os

# Functions
def lightModeImage():
    filetypes = [("Image files", "*.png *.jpg *.jpeg")]

    LMimagePath = filedialog.askopenfilename(title='Select your light mode image', filetypes=filetypes)
    if LMimagePath: 
        LMimagePath = os.path.relpath(LMimagePath)
        print(f"Selected image path: {LMimagePath}")
    else:
        print("No file selected.")

# App config
app = Tk()
app.geometry('750x650')
app.title('Mode')

# Widgets
mainFrame = Frame(app)
mainFrame.pack()

welcomeLabel = Label(mainFrame, text='Welcome to Mode!', font=('Arial', 35))
welcomeLabel.pack()

controlFrame = Frame(app)
controlFrame.pack(padx=20, pady=70, fill=X)

LMimageButton = Button(controlFrame, text='Upload Light Mode image', command=lightModeImage, bg='lightgray', font=('Arial', 15))
LMimageButton.pack(side=LEFT)

app.mainloop()

