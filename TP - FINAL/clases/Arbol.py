from ete3 import PhyloTree, faces, TreeStyle, NodeStyle, AttrFace, TextFace
import subprocess
import tkinter as tk
import os
import time

class Arbol:
    def __init__(self, bootstrap):
        args = ["iqtree","-s","./temp/aligned.fasta", "-B", str(bootstrap), "-redo"]
        self.deleteFasta()
        test = subprocess.Popen(args, stdout=subprocess.PIPE)
        test.communicate()[0]
    
    def getPhyloTree(self):
        # Performs a tree reconciliation analysis 
        gene_tree_nw = self.newick
        genetree = PhyloTree(gene_tree_nw)
        genetree.link_to_alignment(self.alg)
        return genetree, TreeStyle()

    def treeLayout(self, node):
        if node.is_leaf():
            faces.add_face_to_node(AttrFace("name"), node, column=0)
        else:
            node.img_style["size"] = 4
            node.img_style["shape"] = "sphere"
            node.img_style["fgcolor"] = "#AA0000"

    def deleteFasta(self):
        basicRoute = "./temp/aligned.fasta."
        ext = ["treefile","bionj","ckp.gz","contree","iqtree","log","mldist","model.gz","splits.nex","uniqueseq.phy"]
        for x in ext:
            if os.path.exists(basicRoute + x):
                os.remove(basicRoute + x)

    def armarArbol(self):
        # Visualize the reconciled tree
        self.alg = open("./temp/aligned.fasta", "r").read()
        self.newick = open("./temp/aligned.fasta.treefile", "r").read()
        t, ts = self.getPhyloTree()
        ts.scale = 200
        ts.show_leaf_name = False
        ts.show_branch_support = True
        #ts.show_branch_length = True
        ts.layout_fn = self.treeLayout
        t.show(tree_style=ts)