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

        in_file = "fasta.fasta"
        out_file = "aligned.fasta"
        
        clustalomega_cLine = ClustalOmegaCommandline(infile=in_file, outfile=out_file, verbose=True, auto=True, force=True)
        clustalomega_cLine()
            
        os.chdir(owd)
    
    