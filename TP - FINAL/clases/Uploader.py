from tkinter.filedialog import askopenfile
import os


#El fasta debe tener en su cabecera: El nombre | ubicacion | fecha
# >N.... | BS.AS | DATE
class Uploader:
    fastaRoute = "./temp/fasta.fasta"
    ubications = []
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
            return True
        else:
            return False
    
    def parseoUbication(self, fasta):
        record = SeqIO.read(fasta, "fasta")
        for record in SeqIO.parse(handle, "fasta"):
            self.encolarUbications(record.id)
                
    def encolarUbications(self, id):
        cabecera = str(id)        
        return ubication.add(cabecera.split("|")[1])