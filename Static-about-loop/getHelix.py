#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import pandas as pd
import re,os
import numpy as np
#a is two-dimensional array saved the second structure serial number
#in pdbfile secondary structure included 'HELIX' and 'SHEET'
#this function judge whether this line in the secondary structure,in is blank else write in,and flage = 1
#flage can help us find where to insert ‘TER’

def write_line(line, lenth, a):
    flage = 0
    for i in range(0, lenth):
        flage = 0
        if line[21:22].strip() == a[i][0]:
            if int(a[i][1]) < int(line[22:26]) < int(a[i][2]):
                line = ''
                flage = 1
                break
    return flage,line
def get_serial(or_file,new_file,name,a):
    with open(new_file,'a+') as f_new:
        with open(or_file,'r') as f:
            lines = f.readlines()
            for line_pdb in lines:
                line_split2 = line_pdb.split()
                if line_split2[0] == 'HELIX':
                    chainID = line_pdb[19:20].strip()
                    start = line_pdb[21:25].strip()
                    end = line_pdb[33:37].strip()
                    row = ([chainID, start, end])
                    a = np.row_stack((a, row))
                elif line_split2[0] == 'SHEET':
                    chainID = line_pdb[21:22].strip()
                    start = line_pdb[22:26].strip()
                    end = line_pdb[33:37].strip()
                    row = ([chainID, start, end])
                    a = np.row_stack((a, row))
            #print a
            a = a.tolist()
            a = sorted(a, key = (lambda x:x[0]))
            row_lenth = len(a)
            pdb_lenth = len(lines)
            flage1 = flage2 = 0
            for l in range(0,pdb_lenth):
                line_split = lines[l].split()
                if line_split[0] == 'ATOM':
                    flage2,line = write_line(lines[l], row_lenth,a)
                    if flage1 == flage2:
                        f_new.write(line)
                    elif flage1 == 0 and flage2 == 1:
                        if lines[l+1][:4].strip == 'TER':
                            f_new.write(line)
                            print line[l+1]
                            #print 'hahahah'
                        else:
                            f_new.write(line)
                            f_new.write('TER                           ' + name+'\n')
                        flage1 = flage2
                    elif flage1 == 1 and flage2 == 0:
                        f_new.write(line)
                        flage1 = flage2
                elif line_split[0] == 'TER':
                    print lines[l]
                    #f_new.write('TER    ' + name + '\n')
                    f_new.write(lines[l][:26]+'    ' + name + '\n')
                elif line_split[0] =='ENDMDL':
                    f_new.write('END    ' + '\n')
                    break
                elif line_split[0] == 'END':
                    f_new.write('END    ' + '\n')
if __name__ == '__main__':
    '''
    or_file = "/Users/xg666/Desktop/6dek.pdb"
    new_file ='/Users/xg666/Desktop/getTER/loop_test.pdb'
    get_serial(or_file,new_file,a)
    '''
    a = np.zeros(shape=(0,3))
    b = np.zeros(shape=(0,3))
    n = 0
    helixpath = '/Users/xg666/Desktop/gitgao/Static-about-loop/Helixdata/'
    sheetpath ='/Users/xg666/Desktop/gitgao/Static-about-loop/Sheetdata/'
    #f_new = open('/Users/xg666/Desktop/getTER/loop.pdb','a+')
    path =
    filename = os.listdir(path)
    for name in filename:
        or_file = path + name
        get_serial(or_file,new_file,name,a)
        n += 1
        print n
        print name