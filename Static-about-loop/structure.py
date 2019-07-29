import numpy as np
import sys
from numpy import *
def write_line(line, lenth):
    for i in range(0, lenth):
        flage = 0
        #print a[i][0],a[i][1],line[22:26]
        if int(a[i][0]) <= int(line[22:26]) <= int(a[i][1]):
            line = ''
            flage = 1
            break
        else:
            continue
    return flage,line

pdbfile = sys.argv[1]
a = np.zeros(shape=(0,2))
#with open('1crn.pdb','rw') as f:
with open(pdbfile,'rw') as f:
    lines = f.readlines()
    for line in lines:
        line_split = line.split()
        if line_split[0] == 'HELIX':
            start = line[21:25].strip()
            #start = line_split[5]
            #end = line_split[8]
            end = line[33:37].strip()
            row = ([start, end])
            a = np.row_stack((a, row))
        elif line_split[0] == 'SHEET':
            start = line[22:26].strip()
            end = line[33:37].strip()
            row = ([start, end])
            a = np.row_stack((a, row))
        elif line_split[0] == 'TURN':
            print'hellooo'
            start = line_split[6].strip()
            end = line_split[9].strip()
            row = ([start, end])
            a = np.row_stack((a, row))
#sort the arry by the fir column
a = a.tolist()
a = sorted(a, key = (lambda x:x[0]))
#print 'look this!'
print a
#f_new = open('structure_new.pdp','w')
f_new = open('structure_new.pdb','w')
with open(pdbfile,'rw') as f:
#with open('new.pdb','rw') as f:
    lines = f.readlines()
    pdb_lenth = len(lines)
    row_lenth = len(a)
    flage1 = flage2 = 0
    for l in range(0,pdb_lenth):
        line_split = lines[l].split()
        #flage1 = flage2 = 0
        if line_split[0] == 'ATOM':
            flage2, line = write_line(lines[l], row_lenth)
            #print line
            if flage1 == flage2:
                f_new.write(line)
            elif flage1 == 0 and flage2 == 1:
                f_new.write(line)
                f_new.write('TER\n')
                flage1 = flage2
            elif flage1 == 1 and flage2 == 0:
                f_new.write(line)
                flage1 = flage2
        elif line_split[0] == 'END':
            f_new.write('TER\n')
f_new.close()


