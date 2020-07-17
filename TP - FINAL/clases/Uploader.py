from tkinter.filedialog import askopenfile
import Bio.SeqIO as SeqIO
import os



#El fasta debe tener en su cabecera: El nombre | ubicacion | fecha
# >N.... | BS.AS 
# AUCGUCGGU
class Uploader:
    def __init__(self):
        self.fastaRoute = "./temp/fasta.fasta"
        self.ubicaciones = []
    
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
            self.writeFasta(content)
            self.parseoUbication()
            return True
        else:
            return False
    
    def parseoUbication(self):
        for record in SeqIO.parse(self.fastaRoute, "fasta"):
            self.encolarUbications(record)
                
    def encolarUbications(self, record):
        cabecera = str(record.description)  
        ubicacion = cabecera.split("|")[1]
        self.ubicaciones.append(ubicacion)