#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 00:18:48 2017

@author: sgkamal
"""
import pandas as pd
import numpy as np
D = pd.read_csv('data3.csv', header = None)
nD = pd.read_csv('data3.csv', header = None)
for i in range(D.shape[1]):
    #elems = set(D.iloc[:,i])
    #elems = list(elems)
    #elemDict = {}
    #for i1 in range(len(elems)):
    #    elemDict[elems[i1]] = i1
    #T = np.zeros((len(elems), len(elems)))
    
    if i == 0:
        elems = set(D.iloc[:,i])
        elemDict = {}
        for j in D.iloc[:,i]:
            elemDict[j] = elemDict.get(j,0) + 1
        for ii in range(len(D.iloc[:,i])):
            nD.iloc[ii,i] = elemDict[D.iloc[ii,i]]/float(D.shape[0])
    else:
        
        prevElemDict = {}
        currElemDict = {}
        prevElems = list(set(D.iloc[:,i-1]))
        currElems = list(set(D.iloc[:,i]))
        
        for i1 in range(len(prevElems)):
            prevElemDict[prevElems[i1]] = i1
        for i1 in range(len(currElems)):
            currElemDict[currElems[i1]] = i1
        
        T = np.zeros((len(currElems), len(prevElems)))
        
        roster = {} #holds the current elements as keys and the value as a dictionary holding the keys as the elements in the previous column and the count as the value.
        for j in currElems:
            roster[j] = {jj:0 for jj in prevElems}
        for ii in range(len(D.iloc[:,i])):
            roster[D.iloc[ii,i]][D.iloc[ii,i-1]] = roster[D.iloc[ii,i]][D.iloc[ii,i-1]] + 1
        for ltr in roster.keys():
            for ltr2 in roster[ltr]:
                T[(currElemDict[ltr],prevElemDict[ltr2])] = roster[ltr][ltr2]/float(sum(roster[ltr].values()))
        for idx in range(len(D.iloc[:,i])):
            nD.iloc[idx,i] = T[(currElemDict[D.iloc[idx,i]],prevElemDict[D.iloc[idx, i-1]])]

#nD.columns = range(1,61)
table1 = nD.iloc[768:,:30]
table2 = nD.iloc[:768,30:]
table2 = table2.append(nD.iloc[1535:,30:])
table1.columns = range(1,31)
table2.columns = range(1,31)
table1['class'] = [1]*767 + [0]*(table1.shape[0]-767)
table2['class'] = [1]*768 + [0]*(table2.shape[0] - 768)
table1.to_csv('table1.csv', index = False)
table2.to_csv('table2.csv', index = False)