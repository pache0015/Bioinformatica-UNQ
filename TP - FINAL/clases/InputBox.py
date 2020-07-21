from tkinter import messagebox 
import tkinter as tk
  
class InputBox():
    def __init__(self, text=""):
        self.root = tk.Tk()
        self.get = ""
        self.root.geometry("300x100")
        self.root.title("Inputbox")
        self.label_file_name = tk.Label(self.root, text=text)
        self.label_file_name.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.entry.focus()
        self.entry.bind("<Return>", lambda x: self.getinput(self.entry.get()))
        self.root.mainloop()
 
    def getinput(self, value):
        try:
            n = eval(value) 
            if n >= 0 and n <= 1000: 
                self.get = n
                self.root.destroy()
            else:
                messagebox.showinfo(message="Ingrese un valor entre 0 - 1000", title="Vofi")
                self.root.destroy()
        except:
               messagebox.showinfo(message="Solo se deben ingresar numeros", title="Vofi") 
               self.root.destroy()