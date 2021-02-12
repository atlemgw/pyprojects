import tkinter
from time import strftime

vindue = tkinter.Tk()
vindue.title("Mit digitale ur")

# Call Back Funktion
def klokken():
    indhold = strftime("%H:%M:%S")
    tid.config(text = indhold)
    tid.after(1000, klokken)

tid = tkinter.Label(vindue, font = ("calibri", 80, "bold"), background = "purple", foreground = "white")
tid.pack(anchor = "center")

klokken()

vindue.mainloop()
