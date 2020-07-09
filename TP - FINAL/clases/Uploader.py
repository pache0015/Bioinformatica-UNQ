from tkinter.filedialog import askopenfile
import os

class Uploader:
    fastaRoute = "./temp/fasta.fasta"        
    def writeFasta(self, secuence):
        f = open(self.fastaRoute, "w")
        f.write(secuence)
        f.close()
    def deleteFasta(self):
        if os.path.exists(self.fastaRoute):
            os.remove(self.fastaRoute)
    def loadFasta(self):
        file = askopenfile(mode ='r', filetypes =[('Archivos .FASTA', '*.fasta')])
        if file is not None: 
            content = file.read()
            file.close()
            self.deleteFasta()
            #FALTAN LAS VALIDACIONES Y PARSEO DEL FASTA PARA OBTENER DATOS EJ UBICACIONES
            self.writeFasta(content)
        else:
            return False
        return True