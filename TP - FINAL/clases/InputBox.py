from tkinter import messagebox 
import tkinter as tk

class InputBox(object):
    def __init__(self, root, title, text):
        self.choice = None

        # Setup the window
        self.modalWindow = tk.Toplevel(root)
        self.modalWindow.title(title)
        self.modalWindow.resizable(False, False)

        # Setup the widgets in the window
        self.get = ""
        self.modalWindow.geometry("300x100")
        self.modalWindow.title("Ingrese el Bootstrap")
        windowWidth = self.modalWindow.winfo_reqwidth()
        windowHeight = self.modalWindow.winfo_reqheight()

        positionRight = int(self.modalWindow.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(self.modalWindow.winfo_screenheight()/2 - windowHeight/2)
        self.modalWindow.geometry("+{}+{}".format(positionRight, positionDown))
        self.label_file_name = tk.Label(self.modalWindow, text=text)
        self.label_file_name.pack()
        self.entry = tk.Entry(self.modalWindow)
        self.entry.pack()
        self.entry.focus()
        self.entry.bind("<Return>", lambda x: self.getinput(root, self.entry.get()))
        self.modalWindow.rowconfigure(1, minsize = 40)

    def getinput(self, mw, value):
        try:
            n = eval(value) 
            if n >= 1000: 
                self.get = n   
                self.modalWindow.destroy()
            else:
                messagebox.showinfo(message="Debe ingresar valores mayores a 1000, dejando 1000 por default", title="Atención")
                self.get = 1000
                self.modalWindow.destroy()
        except:
               messagebox.showinfo(message="Solo se deben ingresar numeros, dejando 1000 por default", title="Atención")
               self.get = 1000
               self.modalWindow.destroy()
