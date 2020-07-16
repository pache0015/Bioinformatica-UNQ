from ete3 import PhyloTree, faces, TreeStyle, NodeStyle, AttrFace, TextFace
import subprocess
import tkinter as tk
import os

class Arbol:
    def __init__(self):
        self.deleteFasta()
        test = subprocess.Popen(["iqtree","-s","./temp/fasta.fasta", "-B", "1000", "-redo"], stdout=subprocess.PIPE)
        test.communicate()[0]
        self.alg = open("./temp/fasta.fasta", "r").read()
        self.newick = open("./temp/fasta.fasta.treefile", "r").read()
    
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
        if os.path.exists("./temp/fasta.fasta.treefile"):
            os.remove("./temp/fasta.fasta.treefile")

    def armarArbol(self):
        # Visualize the reconciled tree
        t, ts = self.getPhyloTree()
        ts.scale = 200
        ts.show_leaf_name = False
        ts.show_branch_support = True
        #ts.show_branch_length = True
        ts.layout_fn = self.treeLayout
        t.show(tree_style=ts)