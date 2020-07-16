from tkinter import * 
from tkinter.ttk import *
import threading

class progress():
    def __init__(self, parent):
        tk = Tk()
        new = progress(tk)
        but1 = Button(tk, text= 'stop', command= new.end)
        but1.pack()
        
        toplevel = Toplevel(tk)
        self.progressbar = Progressbar(toplevel, orient = HORIZONTAL, mode = 'indeterminate')
        self.progressbar.pack()
        #self.t = threading.Thread()
        #self.t.__init__(target = self.progressbar.start, args = ())
        self.t = threading.Thread(target=self.progressbar.start, args=())
        self.t.start()
        tk.mainloop()

    def end(self):
        if self.t.isAlive() == False:
            self.progressbar.stop()
            self.t.join()
