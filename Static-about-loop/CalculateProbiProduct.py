from Bio.PDB import *
import numpy as np
import generate_NCACN as gn
import math
import sys

def calculate_angle(NCACNlist,i):
    #Rasiduename = NCACNlist[i][17:20].strip()
    # v1 is C,v2 is N,v3 is CA,v4 is C,v5 is N
    v1 = Vector(float(NCACNlist[i-1][30:38]), float(NCACNlist[i-1][38:46]), float(NCACNlist[i-1][46:54]))
    v2 = Vector(float(NCACNlist[i][30:38]), float(NCACNlist[i][38:46]), float(NCACNlist[i][46:54]))
    v3 = Vector(float(NCACNlist[i+1][30:38]), float(NCACNlist[i+1][38:46]), float(NCACNlist[i+1][46:54]))
    v4 = Vector(float(NCACNlist[i+2][30:38]), float(NCACNlist[i+2][38:46]), float(NCACNlist[i+2][46:54]))
    v5 = Vector(float(NCACNlist[i+3][30:38]), float(NCACNlist[i+3][38:46]), float(NCACNlist[i+2][46:54]))
    alpha = vectors.calc_dihedral(v1,v2,v3,v4)
    beta = vectors.calc_dihedral(v2,v3,v4,v5)
    return alpha,beta


def ProbMatrix():
    ProbabMatrix = np.load('densitymatrix.npz')
    return ProbabMatrix

def ProbabilityProduct(TERlist,ProbabMatrix):
    length = len(TERlist)
    ProOfLoop = 1
    #lines = TERlist
    i=0
    probabilitylist = []
    while(i < length):
        if (i == 0):
            i = i + 3
            #print TERlist[i]
            Currname = TERlist[i][17:20].strip()
            #print Currname
            phi,psi = calculate_angle(TERlist,i)
            phi = phi + np.pi
            phi = min(int(math.floor(phi*10/np.pi)),19)
            psi = psi + np.pi
            psi = min(int(math.floor(psi*10/np.pi)),19)
            CurrentRePro = ProbabMatrix[Currname][phi][psi]
            probabilitylist.append(CurrentRePro)
            i = i + 3

        elif (TERlist[i][:4].strip() != 'TER' and TERlist[i+3][:3] != 'TER'):
            Currname = TERlist[i][17:20].strip()
            phi,psi = calculate_angle(TERlist,i)
            phi = phi + np.pi
            phi = min(int(math.floor(phi*10/np.pi)),19)
            psi = psi + np.pi
            psi = min(int(math.floor(psi*10/np.pi)),19)
            CurrentRePro = ProbabMatrix[Currname][phi][psi]
            probabilitylist.append(CurrentRePro)
            i = i + 3
        elif TERlist[i][:4].strip() == 'TER':

            for probability in probabilitylist:
                ProOfLoop = ProOfLoop * probability
            break
        else:
            i = i + 3
    return ProOfLoop,probabilitylist


if __name__ == '__main__':
    args = sys.argv[1:]
    #pdb = args[0]
    #pdb = 'sis9.pdb'
    #pdb = 'sheetlenis7.pdb'
    #path = '/Users/xg666/Desktop/gitgao/Static-about-loop/testdata/lshdata/lenis9/'
    ProbabMatrix = ProbMatrix()

    #print DensityMatrix['CYS']

    #file = path + pdb
    file1 = args[0]
    file2 = args[1]
    with open (file1,'r') as f1:
        loopinfor1 = f1.readlines()
        #for ll in loopinfor:
            #print ll
        #print loopinfor
        TERlist1 = gn.clean_data(loopinfor1)
        #for line in TERlist:
            #print TERlist
            #print line
        ProOfLoop1,probabilitylist1 = ProbabilityProduct(TERlist1,ProbabMatrix)
        ProOfLoop1 = math.log(ProOfLoop1,10)
        print ProOfLoop1
        print probabilitylist1
    with open (file2,'r') as f2:
        loopinfor2 = f2.readlines()
        #for ll in loopinfor:
            #print ll
        #print loopinfor
        TERlist2 = gn.clean_data(loopinfor2)
        #for line in TERlist:
            #print TERlist
            #print line
        ProOfLoop2,probabilitylist2 = ProbabilityProduct(TERlist2,ProbabMatrix)
        ProOfLoop2 = math.log(ProOfLoop2,10)
        print ProOfLoop2
        print probabilitylist2
