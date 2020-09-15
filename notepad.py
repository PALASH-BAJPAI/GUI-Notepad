from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file                         #to make file global variable
    window.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)           #1.0 from line 1, End -till end  delete all


def openFile():
    global file
    #filetype =All files, open all type of files and if text document so .txt
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        window.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")     #open in read mode not appending as that feature is put in save function
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        if file =="":
            file = None
        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            window.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    window.destroy()

def about():
    showinfo("Notepad", "Notepad by Palash Bajpai")
    showinfo("For help contact developer")

if __name__ == '__main__':

    window = Tk()               #to make window
    window.title("Notepad")     #window title
    window.geometry("750x600")  #window size

    #TextArea
    TextArea = Text(window, font="Arial 15")        #typing area
    file = None                                     #points to file we will be typing on
    TextArea.pack(expand=True, fill=BOTH)           #.grid() and pack() are both used for puting on window

    #MENUBAR
    MenuBar = Menu(window)          #make menubar

    #File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)                      #tearoff removes --- in pop all values in new
    FileMenu.add_command(label="New", command=newFile)       # To open new file
    FileMenu.add_command(label="Open", command = openFile)   #To Open already existing file
    FileMenu.add_command(label = "Save", command = saveFile) # To save the current file
    FileMenu.add_separator()                                 #make single horizontal line
    FileMenu.add_command(label = "Exit", command = quitApp)  #to exit app
    MenuBar.add_cascade(label = "File", menu=FileMenu)       #add all above inside File label
    # File Menu ends



    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)
    # Help Menu Ends


    window.config(menu=MenuBar)     #for positioning


    #Adding Scrollbar using rules
    scroller = Scrollbar(TextArea)
    scroller.pack(side=RIGHT,  fill=Y)
    scroller.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroller.set)

    window.mainloop()               #for ending window