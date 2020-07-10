import os
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
import Bio.SeqIO as SeqIO
from Bio.Align.Applications import ClustalOmegaCommandline

class Alineador:
    def alinear(self):
        if os.path.exists("./temp"):
            owd = os.getcwd()
            os.chdir("./temp")
        else:
            print("ERROR - No se puede cambiar la ruta de destino")    

        in_file = "fasta.fasta"
        out_file = "aligned.fasta"
        if !estaAling(in_file):
            clustalomega_cline = ClustalOmegaCommandline(infile=in_file, outfile=out_file, verbose=True, auto=True, force=True)
            clustalomega_cline()
        else:
            f = open('../tem/aligned.fasta', "w")
            f.write(fasta.fasta)
            f.close()
            
        os.chdir(owd)
        
        def estaAling(self, pathFile):
            return True