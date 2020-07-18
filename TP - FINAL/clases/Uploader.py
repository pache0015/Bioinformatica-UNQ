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

    def is_fasta(self, filename):
        with open(filename.name, "rU") as handle:
            try:
                fasta = list(SeqIO.parse(handle, "fasta"))

                if len(fasta) <= 2:
                    raise ValueError()
            except UnicodeDecodeError:
                raise UnicodeDecodeError('type str', b'\x00\x00', 1, 2, 'This is just a fake reason!')       
        return True

    def loadFasta(self):
        file = askopenfile(mode ='r', filetypes =[('Archivos .FASTA', '*.fasta')])
        if file is not None and self.is_fasta(file): 
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
        try:
            ubicacion = cabecera.split("|")[1]
        except IndexError:
            raise ValueError()
        self.ubicaciones.append(ubicacion)