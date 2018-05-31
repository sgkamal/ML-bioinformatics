# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pandas import read_csv
import csv
import os
os.chdir('/Users/sgkamal/Documents/Documents/Courses/ML Bioinformatics/')
fh = open('genomeProject.txt', 'r')
slick = []
for line in fh:
    slick.append(line)
data = {i+1:slick[i].strip().split() for i in range(len(slick))}
#print data
#data = pd.DataFrame(data)
#print data
vals = {'EI,':'Donor', 'IE,':'Acceptor','N,':'Neither'}
print len(data.keys())
for i in data.keys():
    data[i] = [vals[data[i][0]], data[i][-1]]
print data
introns = {'D':[], 'A':[]}
for i in data.keys():
    if data[i][0] == 'Donor':
        introns['D'].append(data[i][-1][30:])
    elif data[i][0] == 'Acceptor':
        introns['A'].append(data[i][-1][:30])
#print introns['A'], introns['D']
#print len(introns['A']), len(introns['D'])
#data = pd.Series(data)
alpha = 0.5
DonNeg = {}
AccNeg = {}
for i in data.keys():
    if data[i][0] == 'Donor' or data[i][0] == 'Neither':
        DonNeg[i] = [data[i][0], data[i][-1]]
    if data[i][0] == 'Acceptor' or data[i][0] == 'Neither':
        AccNeg[i] = [data[i][0], data[i][-1]]
#print DonNeg
#print AccNeg
for i in range(len(DonNeg.keys())):
    DonNeg[i+1] = DonNeg.pop(DonNeg.keys()[i])
for i in range(len(AccNeg.keys())):
    AccNeg[i+1] = AccNeg.pop(AccNeg.keys()[i])
#print DonNeg
#print AccNeg
#print introns
bpvals = {'A':1, 'C':4, 'T':9, 'G':16, 'N': 25,'D': 36,'S': 49,'R':64}
#newdata = []
def change(sequence):
    temp = []
    temp2 = []
    k = range(0,len(sequence), 3)
    #print k
    for i in range(len(k)):
        if not i == len(k)-1:
            for j in range(k[i],k[i+1]):
                temp.append(bpvals[sequence[j]])
        if i == len(k)-1:
            for j in range(k[i],len(sequence)):
                temp.append(bpvals[sequence[j]])
        #print temp
        temp2.append(sum(temp))
        temp = []
    return temp2
#print data
newdata = {}
for i in data.keys():
    newdata[i] = {}
for i in newdata.keys():
    newdata[i][data[i][0]] = change(data[i][1])
print newdata
finallist = []
for i in newdata.keys():
    finallist.append([newdata[i].keys()])
    finallist[-1].append(newdata[i].values())

for i in range(len(finallist)):
    finallist[i].extend(finallist[i][0])
    finallist[i].extend(finallist[i][1][0])
    del finallist[i][0]
    del finallist[i][0]

with open('output.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(finallist)

df = read_csv('output.csv')
df.columns = ['Class', 'Cod1','Cod2','Cod3', 'Cod4','Cod5','Cod6','Cod7','Cod8','Cod9','Cod10','Cod11','Cod12','Cod13','Cod14','Cod15','Cod16','Cod17','Cod18','Cod19','Cod20']
df.to_csv('output2.csv', index = False)

