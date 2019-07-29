import os
#import matplotlib as mpl
#import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
from compiler.ast import flatten

def find_smallestvalue(Array):
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
def get_probability_matrix(AAarr):
    bin =20
    Density = np.zeros((bin,bin))
    x = AAarr[:,0]
    y = AAarr[:,1]
    H, xedges, yedges = np.histogram2d(x,y,bins = bin)
    print xedges.shape,yedges.shape
    ss = H.sum()
    for i in range(0,bin):
        for j in range(0,bin):
            if H[i][j] == 0:
                H[i][j] = find_smallestvalue(H)
            probability = H[i][j] / ss
            Density[i][j] = probability
    sums = Density.sum()
    #new_Density = interpolate.interp2d()
    #print ss
    #print sums
    print Density.shape
    return Density
def generate_density_pyc(path):
    all_file = os.listdir(path)
    all_file.sort()
    ALAarr = np.loadtxt(path + all_file[0])
    ALAdensity = get_probability_matrix(ALAarr)
    print all_file[0]
    print 'ALA'

    ARGarr = np.loadtxt(path + all_file[1])
    ARGdensity = get_probability_matrix(ARGarr)
    print all_file[1]
    print 'ARG'
    ASNarr = np.loadtxt(path + all_file[2])
    ASNdensity = get_probability_matrix(ASNarr)
    print all_file[2]
    print 'ASN'

    ASParr = np.loadtxt(path + all_file[3])
    ASPdensity = get_probability_matrix(ASParr)
    print all_file[3]
    print 'ASP'

    CYSarr = np.loadtxt(path + all_file[4])
    CYSdensity = get_probability_matrix(CYSarr)
    print all_file[4]
    print 'CYSarr'

    GLNarr = np.loadtxt(path + all_file[5])
    GLNdensity = get_probability_matrix(GLNarr)
    print all_file[5]
    print 'GLNarr'

    GLUarr = np.loadtxt(path + all_file[6])
    GLUdensity = get_probability_matrix(GLUarr)
    print all_file[6]
    print 'GLUarr'

    GLYarr = np.loadtxt(path + all_file[7])
    GLYdensity = get_probability_matrix(GLYarr)
    print all_file[7]
    print 'GLYarr'

    HISarr = np.loadtxt(path + all_file[8])
    HISdensity = get_probability_matrix(HISarr)
    print all_file[8]
    print 'HISarr'

    ILEarr = np.loadtxt(path + all_file[9])
    ILEdensity = get_probability_matrix(ILEarr)
    print all_file[9]
    print 'ILEarr'

    LEUarr = np.loadtxt(path + all_file[10])
    LEUdensity = get_probability_matrix(LEUarr)
    print all_file[10]
    print 'LEUarr'

    LYSarr = np.loadtxt(path + all_file[11])
    LYSdensity = get_probability_matrix(LYSarr)
    print all_file[11]
    print 'LYSarr'
    METarr = np.loadtxt(path + all_file[12])
    METdensity = get_probability_matrix(METarr)
    print all_file[12]
    print 'METarr'
    PHEarr = np.loadtxt(path + all_file[13])
    PHEdensity= get_probability_matrix(PHEarr)
    print all_file[13]
    print 'PHEarr'

    PROarr = np.loadtxt(path + all_file[14])
    PROdensity = get_probability_matrix(PROarr)
    print all_file[14]
    print 'PROarr'

    SERarr = np.loadtxt(path + all_file[15])
    SERdensity = get_probability_matrix(SERarr)
    print all_file[15]
    print 'SERarr'

    THRarr = np.loadtxt(path + all_file[16])
    THRdensity = get_probability_matrix(THRarr)
    print all_file[16]
    print 'THRarr'

    TRParr = np.loadtxt(path + all_file[17])
    TRPdensity = get_probability_matrix(TRParr)
    print all_file[17]
    print 'TRParr'

    TYRarr = np.loadtxt(path + all_file[18])
    TYRdensity = get_probability_matrix(TYRarr)
    print all_file[18]
    print 'TYRarr'

    VALarr = np.loadtxt(path + all_file[19])
    VALdensity = get_probability_matrix(VALarr)
    print all_file[19]
    print 'VALarr'
    np.savez('DensMatForStand.npz',ALA = ALAdensity,ARG = ARGdensity,ASN = ASNdensity,ASP = ASPdensity,CYS = CYSdensity,GLN = GLNdensity,GLU = GLUdensity,\
        GLY = GLYdensity,HIS = HISdensity,ILE = ILEdensity,LEU = LEUdensity,LYS = LYSdensity,MET = METdensity,PHE = PHEdensity,PRO = PROdensity,SER = SERdensity,THR =THRdensity,TRP = TRPdensity,TYR =TYRdensity,VAL = VALdensity)
    DensityMatrix = np.load('densitymatrix.npz')
    #print DensityMatrix
    return DensityMatrix
if __name__ == '__main__':
    path = '/Users/xg666/Desktop/loop/getTER/standard/angledatafinally/'
    #path = '/Users/xg666/Desktop/loop/getTER/moreloopdata/angleresult/'
    #all_file = os.listdir(path)
    #all_file.sort()
    #ALAarr = np.loadtxt(path + all_file[0])
    #ALAdensity = get_probability_matrix(ALAarr)
    DensityMatrix = generate_density_pyc(path)
    #DensityMatrix = np.load('DensMatForStand.npz')
    #print type(DensityMatrix)
    #print DensityMatrix['ALA'][19][19]
    #generate_density_pyc(path)
