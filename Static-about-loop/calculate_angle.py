from Bio.PDB import *
import numpy as np
def calculateAngle(NCAVNlist,i):
    lines = NCAVNlist
    length = len(lines)
    i = 0
    while (i < length):
        if (i == 0):
            print i
            i = i + 3
            Residuename = lines[i][17:20].strip()
                # v1 is C,v2 is N,v3 is CA,v4 is C,v5 is N
            v1 = Vector(float(lines[i-1][30:38]), float(lines[i-1][38:46]), float(lines[i-1][46:54]))
            v2 = Vector(float(lines[i][30:38]), float(lines[i][38:46]), float(lines[i][46:54]))
            v3 = Vector(float(lines[i+1][30:38]), float(lines[i+1][38:46]), float(lines[i+1][46:54]))
            v4 = Vector(float(lines[i+2][30:38]), float(lines[i+2][38:46]), float(lines[i+2][46:54]))
            v5 = Vector(float(lines[i+3][30:38]), float(lines[i+3][38:46]), float(lines[i+2][46:54]))
            alpha = vectors.calc_dihedral(v1,v2,v3,v4)
            beta = vectors.calc_dihedral(v2,v3,v4,v5)
        elif (lines[i][:3] == 'TER'):
            break
    return Residuename,alpha,beta


