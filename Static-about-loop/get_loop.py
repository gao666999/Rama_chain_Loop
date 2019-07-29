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
def write_line(line, lenth):
    for i in range(0, lenth):
        flage = 0
        global flage
        if int(a[i][0]) <= int(line[22:26]) < int(a[i][1]):
            line = ''
            flage = 1
            break
        else:
            continue
    return flage,line

def get_serial(or_file,new_file):
    f_new = open(new_file,'a+')
    with open(or_file,'r') as f:
        lines = f.readlines()
        for line_pdb in lines:
            line_split2 = line_pdb.split()
            if line_split2[0] == 'HELIX':
                start = line_pdb[21:25].strip()
                end = line_pdb[33:37].strip()
                row = ([start, end])
                a = np.row_stack((a, row))
            elif line_split2[0] == 'SHEET':
                start = line_pdb[22:26].strip()
                end = line_pdb[33:37].strip()
                row = ([start, end])
                a = np.row_stack((a, row))
        a = a.tolist()
        a = sorted(a, key = (lambda x:x[0]))
        pdb_lenth = len(lines)
        row_lenth = len(a)
        flage1 = flage2 = 0
        for l in range(0,pdb_lenth):
            line_split = lines[l].split()
            if line_split[0] == 'ATOM':
                flage2,line = write_line(lines[l], row_lenth)
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
    f_new.write('TER\n')
    f_new.write(or_file)
    f_new.close()

if __name__ == '__main__':
    or_file = "/Users/xg666/Desktop/6dek.pdb"
    new_file ='/Users/xg666/Desktop/getTER/loop.pdb'
    get_serial(or_file,new_file)
