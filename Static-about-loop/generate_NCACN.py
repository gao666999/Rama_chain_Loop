import numpy as np
import os
def clean_data(Residuelines):
    NCACNList = []
    temp_atom = []
    temp_residues = []
    Re_order = 0
    Residue_number = 0
    lines = Residuelines
    length = len(lines)
    for i in range(0,length):
        if lines[i][:4].strip() == 'ATOM':
            # to make sure whether this residue has N,CA and C
            if lines[i][13:17].strip() == 'N' and lines[i+1][13:17].strip() == 'CA' and lines[i+2][13:17].strip() == 'C':
                # to make sure these atoms are belong to the same residue
                if lines[i][22:26].strip() == lines[i+1][22:26].strip() == lines[i+2][22:26].strip():
                    # make sure to start from the first residue
                    if Re_order == 0:
                        Re_order = int(lines[i][22:26].strip())
                        temp_atom.append(lines[i])
                        temp_atom.append(lines[i+1])
                        temp_atom.append(lines[i+2])
                        for t_atom in temp_atom:
                            temp_residues.append(t_atom)
                        Residue_number += 1
                        temp_atom = []
                    else:
                        current_order = int(lines[i][22:26].strip())
                        if current_order == Re_order +1:
                            temp_atom.append(lines[i])
                            temp_atom.append(lines[i+1])
                            temp_atom.append(lines[i+2])
                            for t_atom in temp_atom:
                                temp_residues.append(t_atom)
                            Residue_number += 1
                            Re_order = current_order
                            temp_atom = []
                        else:
                            if Residue_number >= 3:
                                for t_residue in temp_residues:
                                    NCACNList.append(t_residue)
                                    print t_residue
                                NCACNList.append('TER\n')
                                Residue_number = 0
                                temp_residues = []
                            else:
                                Re_order = 0
                                Residue_number = 0
                                temp_residues = []
                                continue
                else:
                    if Residue_number >= 3:
                        for t_residue in temp_residues:
                            NCACNList.append(t_residue)
                        NCACNList.append('TER\n')
                        Re_order = 0
                        Residue_number = 0
                        temp_residues = []
                    else:
                        Residue_number = 0
                        temp_residues = []
                        continue
            else:
                continue
        elif lines[i][:4].strip() == 'TER':
            if Residue_number >= 3:
                for t_residue in temp_residues:
                    NCACNList.append(t_residue)
                    #print t_residue
                #print lines[i]
                NCACNList.append(lines[i])
                Residue_number = 0
                temp_residues = []
            else:
                Residue_number = 0
                temp_residues = []
                continue
        else:
            continue
    return NCACNList