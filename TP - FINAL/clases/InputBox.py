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
        if(eval(self.get))
        x = 1 y = 2 (print(x+y))
        x = "1" y = "2" (print(x+y))
        self.root.mainloop()
 
    def getinput(self, value):
        self.get = value
        self.root.destroy()
