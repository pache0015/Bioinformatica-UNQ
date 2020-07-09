from ete3 import PhyloTree, faces, TreeStyle, NodeStyle
import subprocess

class Arbol:
    def __init__(self):
        test = subprocess.Popen(["iqtree","-s","./temp/fasta.fasta"], stdout=subprocess.PIPE)
        test.communicate()[0]
        self.alg = open("./temp/fasta.fasta", "r").read()
        self.newick = open("./temp/fasta.fasta.treefile", "r").read()
    
    def getPhyloTree(self):
        # Performs a tree reconciliation analysis 
        gene_tree_nw = self.newick
        genetree = PhyloTree(gene_tree_nw)
        genetree.link_to_alignment(self.alg)
        return genetree, TreeStyle()

    def armarArbol(self):
        # Visualize the reconciled tree
        t, ts = self.getPhyloTree()
        ts.scale = 20
        ts.show_leaf_name = True
        ts.show_branch_length = True
        ts.show_branch_support = True
        t.show(tree_style=ts)