from Bio.PDB import *
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB import PDBIO
from Bio.PDB import Select
import numpy as np
import math
import sys
from compiler.ast import flatten


def calculate_angle(residueslist,i):
    #Rasiduename = NCACNlist[i][17:20].strip()
    # v1 is C,v2 is N,v3 is CA,v4 is C,v5 is N
    if residueslist[i-1].has_id('C') and residueslist[i].has_id('N') and residueslist[i].has_id('CA') \
    and residueslist[i].has_id('C') and residueslist[i+1].has_id('N'):
        #print '+++++++++++++++++++++++'
        #print residueslist[i].get_id()
        #print i
        v1 = residueslist[i-1]['C'].get_vector()
        v2 = residueslist[i]['N'].get_vector()
        v3 = residueslist[i]['CA'].get_vector()
        v4 = residueslist[i]['C'].get_vector()
        v5 = residueslist[i+1]['N'].get_vector()
        alpha = vectors.calc_dihedral(v1,v2,v3,v4)
        beta = vectors.calc_dihedral(v2,v3,v4,v5)
        #print alpha,beta
        return alpha,beta
def get_smallest_probability(Probabmatrix,Currname):
    Array = Probabmatrix[Currname]
    #print type(Array)
    value_list = flatten(Array)
    #value_list.totist()
    value_list = Array.reshape((1,400)).tolist()
    value_list = value_list[0]
    value_list.sort()
    length = len(value_list)
    for i in range(0,length):
        if value_list[i] != 0:
            break
    return value_list[i]

def ProMatrix():
    ProbabMatrixforLoop = np.load('/Users/xg666/Desktop/Three-dimensional-structure-prediction/loopprobability/densitymatrix.npz')
    ProbabMatrixforStand = np.load('/Users/xg666/Desktop/Three-dimensional-structure-prediction/loopprobability/DensMatForStand.npz')
    return ProbabMatrixforLoop,ProbabMatrixforStand
def get_residues_length(residues):
    LengthOfResidue = 0
    residueslist = []
    for residue in residues:
        residueslist.append(residue)
        LengthOfResidue += 1
    return LengthOfResidue,residueslist

def ProbabilityProduct(pdbfile,ProbabMatrixforLoop,ProbabMatrixforStand):
    p = PDBParser(PERMISSIVE = 1)
    structure_id = pdbfile
    structure = p.get_structure(structure_id,pdbfile)
    model = structure[0]
    residues = model.get_residues()
    length,residueslist = get_residues_length(residues)
    #smallest_probabilityl = get_smallest_probability(ProbabMatrixforLoop)
    #smallest_probabilitys = get_smallest_probability(ProbabMatrixforStand)
    #print length
    ProOfLoopl = 0
    ProOfLoops = 0
    #lines = TERlist
    i = 1
    probabilitylistl = []
    probabilitylists = []
    if length <= 3:
        print 'the length of loop should be longer than 3'
        exit()
    while (i < length - 1):
        if residueslist[i-1].has_id('C') and residueslist[i].has_id('N') and residueslist[i].has_id('CA') \
        and residueslist[i].has_id('C') and residueslist[i+1].has_id('N'):
            v1 = residueslist[i-1]['C'].get_vector()
            v2 = residueslist[i]['N'].get_vector()
            v3 = residueslist[i]['CA'].get_vector()
            v4 = residueslist[i]['C'].get_vector()
            v5 = residueslist[i+1]['N'].get_vector()
            phi = vectors.calc_dihedral(v1,v2,v3,v4)
            psi = vectors.calc_dihedral(v2,v3,v4,v5)
            #phi,psi = calculate_angle(residueslist,i)
            Currname = residueslist[i].get_resname()
            phi = phi + np.pi
            phi = min(int(math.floor(phi*10/np.pi)),19)
            psi = psi + np.pi
            psi = min(int(math.floor(psi*10/np.pi)),19)
            CurrentReProl = 10 * ProbabMatrixforLoop[Currname][phi][psi]
            #print CurrentReProl
            #print 'vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv'
            if CurrentReProl == 0:
                #print 'nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn'
                CurrentReProl = get_smallest_probability(ProbabMatrixforLoop,Currname)
                #print CurrentReProl
            CurrentRePros = 10 * ProbabMatrixforStand[Currname][phi][psi]
            if CurrentRePros == 0:
                #print 'sssssssssssssssssssssssssssssssss'
                CurrentRePros = get_smallest_probability(ProbabMatrixforStand,Currname)
                #print CurrentRePros
            probabilitylistl.append(CurrentReProl)
            probabilitylists.append(CurrentRePros)
        i = i + 1
    for probabilityl in probabilitylistl:
        #probabilityl = 5 * probabilityl
        probabilityl = math.log(probabilityl,10)
        #if probabilityl == 0:
        #print probabilityl
        ProOfLoopl = ProOfLoopl + probabilityl
        #print ProOfLoopl
    #ProOfLoopforl = math.log(ProOfLoopl,10)
    for probabilitys in probabilitylists:
        #probabilitys = 5 * probabilitys
        probabilitys = math.log(probabilitys,10)
        #print probabilityss
        ProOfLoops = ProOfLoops + probabilitys
    #ProOfLoopfors = math.log(ProOfLoops,10)
    #print '*******************************'
    #print ProOfLoopforl,ProOfLoopfors
    return ProOfLoopl,ProOfLoops


if __name__ == '__main__':
    args = sys.argv[1:]
    ProbabMatrixforLoop,ProbabMatrixforStand = ProMatrix()
    pdbfile = args[0]
    ProOfLoopbasedLoop,ProOfLoopbasedStand = ProbabilityProduct(pdbfile,ProbabMatrixforLoop,ProbabMatrixforStand)
    print ProOfLoopbasedLoop,ProOfLoopbasedStand

