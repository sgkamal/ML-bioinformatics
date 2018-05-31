#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 18:46:32 2017

@author: sgkamal
"""
import os
os.chdir('/Users/sgkamal/Documents/Documents/Courses/ML Bioinformatics')
import pandas as pd
import numpy as np

data3 = pd.read_csv('data3.csv')
dd1 = pd.read_csv('accneg1.csv')
dd2 = pd.read_csv('donneg1.csv')
classes = pd.read_csv('output.csv')
new1 = pd.DataFrame()
new2 = pd.DataFrame()
new1 = new1.append(data3.iloc[:768,:])
new1 = new1.append(data3.iloc[1535:,:])
new2 = new2.append(data3.iloc[768:,:])
new2.columns = range(1,61)
new1.columns = range(1,61)
new2.to_csv('2.csv', index = False)
new1.to_csv('1.csv', index = False)
new1.columns = range(1,61)
data3.columns = range(1,61)


sumss = np.zeros(data3.shape[1])
sums1 = np.zeros(dd1.shape[1] - 1)
sums2 = np.zeros(dd2.shape[1] - 1)
univals3 = dict()
univals = dict()
univals2 = dict()
newvals = {}
newvals2 = {}

print set(dd1.iloc[:,1])
for i in range(dd1.shape[1]-1):
        sums1[i] = sum(dd1.iloc[:,i])
for i in range(dd2.shape[1]-1):
        sums2[i] = sum(dd1.iloc[:,i])
for k in range(dd1.shape[1]-1):
    for i in range(dd1.shape[0]):
        univals[dd1.iloc[i,k]] = univals.get(dd1.iloc[i,k],0) + 1
    for i in range(dd1.shape[0]):
        dd1.iloc[i,k] = dd1.iloc[i,k]*univals[dd1.iloc[i,k]]/sums1[k]
    #print dd1.iloc[:,1]

for k in range(dd2.shape[1]-1):
    for i in range(dd2.shape[0]):
        univals2[dd2.iloc[i,k]] = univals2.get(dd2.iloc[i,k],0) + 1
    for i in range(dd2.shape[0]):
        dd2.iloc[i,k] = dd2.iloc[i,k]*univals2[dd2.iloc[i,k]]/sums2[k]

dd1.columns = range(11)

dd2.columns = range(11)
dd1.to_csv('accneg1.csv', index = False)
dd2.to_csv('donneg1.csv', index = False)




for k in range(data3.shape[1]):
    for i in range(data3.shape[0]):
        univals3[data3.iloc[i,k]] = univals3.get(data3.iloc[i,k],0) + 1
    for i in range(data3.shape[0]):
        data3.iloc[i,k] = float(univals3[data3.iloc[i,k]])/data3.shape[0]
        
for k in range(new1.shape[1]):
    for i in range(new1.shape[0]):
        newvals[new1.iloc[i,k]] = newvals.get(new1.iloc[i,k],0) + 1
    for i in range(new1.shape[0]):
        new1.iloc[i,k] = float(newvals[new1.iloc[i,k]])/new1.shape[0]

for k in range(new2.shape[1]):
    for i in range(new2.shape[0]):
        newvals2[new2.iloc[i,k]] = newvals2.get(new2.iloc[i,k],0) + 1
    for i in range(new2.shape[0]):
        new2.iloc[i,k] = float(newvals2[new2.iloc[i,k]])/new2.shape[0]




#data3.to_csv('dataa.csv', index = False)
data3['class'] = classes.iloc[:,0]
new1['class'] = dd2.iloc[:,10]
data3.to_csv('dataa.csv', index = False)
univals3
for i in range(data3.shape[0]):
    if data3.iloc[i,60] == 'Donor':
        data3.iloc[i,60] = 1
    elif data3.iloc[i,60] == 'Acceptor':
        data3.iloc[i,60] = 2
    else:
        data3.iloc[i,60] = 3

data3.to_csv('dataa.csv', index = False)


