from tkinter import *
from tkinter import filedialog, messagebox 
from PIL import Image, ImageTk
import os
from appscript import app as apple_app, mactypes

# Global variables for img paths & last mode
LMimagePath = ""
DMimagePath = ""
lastMode = None

# Functions
def lightModeImage():
    global LMimagePath
    filetypes = [("Image files", "*.png *.jpg *.jpeg")]

    LMimagePath = filedialog.askopenfilename(title='Select your light mode image wallpaper', filetypes=filetypes)
    if LMimagePath:
        LMimagePath = os.path.abspath(LMimagePath)
        print(f"Selected image path: {LMimagePath}")

        image = Image.open(LMimagePath)
        image.thumbnail((150, 150))
        LMimage = ImageTk.PhotoImage(image)

        LMimagePreview.config(image=LMimage)
        LMimagePreview.image = LMimage
        
    else:
        print("No file selected.")
        LMimagePreview.config(image='')

def darkModeImage():
    global DMimagePath
    filetypes = [("Image files", "*.png *.jpg *.jpeg")]

    DMimagePath = filedialog.askopenfilename(title='Select your dark mode image wallpaper', filetypes=filetypes)
    if DMimagePath:
        DMimagePath = os.path.abspath(DMimagePath)
        print(f"Selected image path: {DMimagePath}")

        image = Image.open(DMimagePath)
        image.thumbnail((150, 150))
        DMimage = ImageTk.PhotoImage(image)

        DMimagePreview.config(image=DMimage)
        DMimagePreview.image = DMimage
        
    else:
        print("No file selected.")
        DMimagePreview.config(image='')

def setWallpaper():
    global lastMode
    try:
        systemEvents = apple_app('System Events')
        appearancePref = systemEvents.appearance_preferences.get()
        darkMode = appearancePref.dark_mode.get()

        if darkMode:
            if DMimagePath:
                try:
                    DMwallpaper = mactypes.File(DMimagePath)
                    apple_app('Finder').desktop_picture.set(DMwallpaper)
                except Exception as e:
                    messagebox.showinfo("Message", f"An error occurred: {e}")
            else:
                messagebox.showinfo("Message", "No Dark Mode image selected.")
        else:
            if LMimagePath:
                try:
                    LMwallpaper = mactypes.File(LMimagePath)
                    apple_app('Finder').desktop_picture.set(LMwallpaper)
                except Exception as e:
                    messagebox.showinfo("Message", f"An error occurred: {e}")
            else:
                messagebox.showinfo("Message", "No Light Mode image selected.")
                
        lastMode = darkMode

    except Exception as e:
        messagebox.showinfo("Message", f"Error: {e}")

def monitorAppearance():
    global lastMode
    try:
        systemEvents = apple_app('System Events')
        appearancePref = systemEvents.appearance_preferences.get()
        darkMode = appearancePref.dark_mode.get()

        if lastMode is None:
            lastMode = darkMode

        if darkMode != lastMode:
            setWallpaper()

        root.after(5000, monitorAppearance)

    except Exception as e:
        messagebox.showinfo("Message", f"Error: {e}")

# App config
root = Tk()
root.geometry('800x700')
root.title('Mode')

# Widgets
mainFrame = Frame(root)
mainFrame.pack()

welcomeLabel = Label(mainFrame, text='Welcome to Mode!', font=('Arial', 35))
welcomeLabel.pack()

controlFrame = Frame(root)
controlFrame.pack(padx=20, pady=70, fill=X)

# LIGHT MODE WIDGETS
LMimageButton = Button(controlFrame, text='Upload Light Mode image', command=lightModeImage, bg='lightgray', font=('Arial', 15))
LMimageButton.pack()

LMimagePreview = Label(controlFrame, bg='white', width=150, height=150, borderwidth=2, relief='solid')
LMimagePreview.pack(padx=20, pady=20)

# DARK MODE WIDGETS
DMimageButton = Button(controlFrame, text='Upload Dark Mode image', command=darkModeImage, bg='lightgray', font=('Arial', 15))
DMimageButton.pack()

DMimagePreview = Label(controlFrame, bg='white', width=150, height=150, borderwidth=2, relief='solid')
DMimagePreview.pack(padx=20, pady=20)

# SET MODE
setModeButton = Button(controlFrame, text='Set Mode!', command=setWallpaper, bg='red', font=('Arial', 15))
setModeButton.pack(padx=20, pady=20)

# Start monitoring
monitorAppearance()

# App mainloop
root.mainloop()
