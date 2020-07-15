# coding=utf-8

from PIL import Image, ImageTk
from tkinter import PhotoImage, messagebox
from clases.Arbol import Arbol
from clases.Mapa import Mapa, UbicacionNotFound
from clases.Uploader import Uploader
from clases.Alineador import Alineador
from tkinterhtml import HtmlFrame
import tkinter as tk

lista_de_nombre_de_ubicaciones = ["Londres", "Paris", "Amsterdam", "Las Vegas", "Tokyo", "Buenos Aires", "San Pablo", "Tijuana", "Medellin", "Texas", "Nueva Orleans"]

class Handler():
    def __init__(self):
        self.flag_map = False
        self.flag_upload = False
        self.flag_align = False
        
    
    def client_exit(self):
        root.destroy()
        
    def upload_fasta(self):        
        uploader = Uploader()
        if uploader.loadFasta():
            self.flag_upload = True
            messagebox.showinfo(message="Se cargo el FASTA correctamente", title="")
        else:
            messagebox.showinfo(message="No se cargo el FASTA", title="")
            
    def align_secuences(self):
        if self.flag_upload:
            alineador = Alineador()
            alineador.alinear()
            #Aca iria el loading
            self.flag_align = True
            messagebox.showinfo(message="Alineado amewo!", title="")
        else:
            messagebox.showinfo(message="Carga primero el FASTA, titan", title="")
        
        
    def make_tree(self):
        if self.flag_upload and self.flag_align:
            arbol = Arbol()
            #Aca iria el loading
            arbol.armarArbol()
        else:
            messagebox.showinfo(message="Primero carga y alinea, mostro", title="")
        
    def make_map(self):
        mapa = Mapa()
        try:
            if not self.flag_map:
                self.flag_map = True
                root = tk.Tk()
                frame = HtmlFrame(root, horizontal_scrollbar="auto")
                mapita = mapa.armar_mapa(lista_de_nombre_de_ubicaciones).render_mapa()
                mapa.guardar_mapa()
        except UbicacionNotFound as e:
            messagebox.showinfo("Ojo al piojo", str(e))
            

class BkgrFrame(tk.Frame):
    def __init__(self, parent, file_path, width, height):
        super(BkgrFrame, self).__init__(parent, borderwidth=0, highlightthickness=0)

        self.canvas = tk.Canvas(self, width=width, height=height)
        self.canvas.pack()

        pil_img = Image.open(file_path)
        self.img = ImageTk.PhotoImage(pil_img.resize((width, height), Image.ANTIALIAS))
        self.bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)

    def add(self, widget, x, y):
        canvas_window = self.canvas.create_window(x, y, anchor=tk.NW, window=widget)
        return widget


if __name__ == '__main__':

    IMAGE_PATH = './img/MenuHerramientaBio.png'
    WIDTH, HEIGTH = 800, 600

    root = tk.Tk()
    root.geometry('{}x{}'.format(WIDTH, HEIGTH))
    
    handler = Handler()

    bkrgframe = BkgrFrame(root, IMAGE_PATH, WIDTH, HEIGTH)
    bkrgframe.pack()
    
    exitPhot = PhotoImage(file = r"./img/BotonSalir.png")
    fastaPhot = PhotoImage(file = r"./img/BotonFasta.png")
    alignPhot = PhotoImage(file = r"./img/BotonAlinear.png")
    treePhot = PhotoImage(file = r"./img/BotonArbolear.png")
    mapPhot = PhotoImage(file = r"./img/BotonMapear.png")

    button1 = bkrgframe.add(tk.Button(root, image=exitPhot, command= handler.client_exit), 650, 8)
    button2 = bkrgframe.add(tk.Button(root, image=fastaPhot, command= handler.upload_fasta), 310, 180)
    button3 = bkrgframe.add(tk.Button(root, image=alignPhot, command= handler.align_secuences), 65, 340)
    button4 = bkrgframe.add(tk.Button(root, image=treePhot, command= handler.make_tree), 65, 430)
    button5 = bkrgframe.add(tk.Button(root, image=mapPhot, command= handler.make_map), 60, 520)

    root.resizable(width=False, height=False)
    root.wm_attributes('-type', 'splash')
    root.mainloop()
