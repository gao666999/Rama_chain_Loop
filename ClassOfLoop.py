#this calss's object is loop or chain or any other list of Residues
import numpy as np
import math
class AminoAcid:
    def __init__(self,ter_list):
        self.number_of_NN = 0
        self.center_of_NN_list = []
        self.number_of_atom = 0
        self.center_of_TER = []
        self.distance = 0
        self.radius = 0
        self.TER_list = ter_list
        self.RadiusGyration = 0
    #Sum all atom coordinate
    def sumCenters(self,temp_list_of_atom):
        Amount_of_atom = 0
        list_of_xyz = np.zeros([3,])
        center = np.zeros([3,1])
        for line in temp_list_of_atom:
            x = float(line[30:38])
            y = float(line[38:46])
            z = float(line[46:54])
            #sum a data of AmnioAcid
            list_of_xyz[0] += x
            list_of_xyz[1] += y
            list_of_xyz[2] += z
            Amount_of_atom += 1
        center[0] = list_of_xyz[0] / Amount_of_atom
        center[1] = list_of_xyz[1] / Amount_of_atom
        center[2] = list_of_xyz[2] / Amount_of_atom
        return center, Amount_of_atom

    #Calculate the center of the amino acid
    def calculateCenterOfTer(self):
        x = 0
        y = 0
        z = 0
        if(self.number_of_NN == 0):
            return False
        else:
            #print self.center_of_NN_list
            for i in range(0, self.number_of_NN):
                print i
                x += self.center_of_NN_list[i][0]
                y += self.center_of_NN_list[i][1]
                z += self.center_of_NN_list[i][2]
        self.center_of_TER.append(x / self.number_of_NN)
        self.center_of_TER.append(y / self.number_of_NN)
        self.center_of_TER.append(z / self.number_of_NN)

    # calculate the length of a chain,and return the length and center of a chain
    def calculateNumberOfNNInTER(self):
        flaga = 'flag'
        temp_list_of_atom = []
        temp_number_of_atom = 0
        for line in self.TER_list:
            flagb = line[22:26].strip()
            if line[:4].strip() =='ATOM':
                if flaga != flagb and flaga == 'flag':
                    temp_list_of_atom.append(line)
                    flaga = flagb
                    #self.number_of_NN = self.number_of_NN + 1
                elif flaga != flagb and flaga != 'flag':
                    temp_center_of_NN, temp_number_of_atom = self.sumCenters(temp_list_of_atom)
                    self.center_of_NN_list.append(temp_center_of_NN)
                    #self.number_of_atom += temp_number_of_atom
                    temp_list_of_atom = []
                    temp_list_of_atom.append(line)
                    self.number_of_NN = self.number_of_NN + 1
                    flaga = flagb
                else:
                    temp_list_of_atom.append(line)
                    continue
            elif line[:3].strip() == 'TER':
                temp_center_of_NN, number_of_atom = self.sumCenters(temp_list_of_atom)
                self.center_of_NN_list.append(temp_center_of_NN)
                temp_list_of_atom = []
            else:
                break
        print self.number_of_NN
        print "number of NN"
        if self.number_of_NN == 0:
            print self.TER_list

    def distanceOfTer(self):#chain_length
        self.distance = math.sqrt(pow(self.center_of_NN_list[0][0] - self.center_of_NN_list[-1][0],2) + pow(self.center_of_NN_list[0][1] - self.center_of_NN_list[-1][1] ,2) + pow(self.center_of_NN_list[0][2] - self.center_of_NN_list[-1][2],2))
        self.distance = float('%.4f'%self.distance)
        print type(self.distance)
        #print 'dddddd'
        return self.distance

    def getRadiusOfGyration(self):
     #center of gravity, assuming all atoms have equal weight
        sum_Rg2 = 0
        #print self.center_of_NN_list
        #print self.center_of_TER
        for list_sub2 in self.center_of_NN_list:
            sum_Rg2 += (list_sub2[0]-self.center_of_TER[0])**2+(list_sub2[1]-self.center_of_TER[1])**2+(list_sub2[2]-self.center_of_TER[2])**2
        #result=[rc,(1.0*sum_Rg2/n)**0.5]
        #print sum_Rg2
        self.RadiusGyration = (1.0*sum_Rg2/self.number_of_NN)**0.5
        self.RadiusGyration = float('%.4f'%self.RadiusGyration)
        if math.isnan(self.RadiusGyration):
            print self.TER_list
        #print self.RadiusGyration
        return self.RadiusGyration
    def getRadius(self):
        sumRg = 0
        RadiusList = []
        for AAcenter in self.center_of_NN_list:
            sumRg = (AAcenter[0]-self.center_of_TER[0])**2+(AAcenter[1]-self.center_of_TER[1])**2+(AAcenter[2]-self.center_of_TER[2])**2
            print sumRg
            temRadius = (1.0*sumRg)**0.5
            temRadius = float('%.4f'%temRadius)
            RadiusList.append(temRadius)
            temRadius = 0
        RadiusList = sorted(RadiusList)
        #print RadiusList
        print "this is RadiusList"
        self.radius = RadiusList[-1]
        print type(self.radius)
        print self.radius
        return self.radius

    def getNuberOfNN(self):
        return self.number_of_NN
