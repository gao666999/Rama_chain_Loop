import os
from Bio.PDB import *
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB import PDBIO
from Bio.PDB import Select
from multiprocessing import Pool
import multiprocessing
import sys
# rewrite ResidueSelect class,so that PDBIO can use this class to save the structure we want
class ResidueSelect(Select):
    def __init__(self,id1,id2):
        self.id1 = id1
        self.id2 = id2

    def accept_residue(self,residue):
        if residue.get_parent().get_id() =='A':
            #print residue.get_id()[1]
            if self.id1 <= residue.get_id()[1] <= self.id2:
            #print residue.get_id()[1]
                return True
        else:
            return False
# this function can return a list contain all the file'name in one directory excpte .Dstore
def listdirInMac(path):
    os_list = os.listdir(path)
    for item in os_list:
        if item.startswith('.') and os.path.isfile(os.path.join(path, item)):
            os_list.remove(item)
    return os_list
#use Bio.PDB create the pdb strcuture
def make_structure_for_pdbfile(file,structure_id):
    p = PDBParser(PERMISSIVE = 1)
    structure = p.get_structure(structure_id,file)
    return structure
#save the loop
def save_loop(globalfile,structure_id,loopfile,id1,id2):
    structure = make_structure_for_pdbfile(globalfile,structure_id)
    io = PDBIO()
    p = PDBParser(PERMISSIVE = 1)
    io.set_structure(structure)
    io.save(loopfile, ResidueSelect(id1,id2))

if __name__ == "__main__":
    args=sys.argv[1:]
    globalfile=args[0]
    structure_id=args[1]
    loopfile=args[2]
    id1=args[3]
    id2=args[4]
    save_loop(globalfile,structure_id,loopfile,id1,id2)

