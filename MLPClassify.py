#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 04:58:05 2017

@author: sgkamal
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.cross_validation import train_test_split

data1 = pd.read_csv('table1.csv')
data2 = pd.read_csv('table2.csv')
df1_x = data1.iloc[:,:30]
#print df_x
df1_y = data1.iloc[:,30]
#print df_y
df2_x = data2.iloc[:,:30]
#print df_x
df2_y = data2.iloc[:,30]

x1_train, x1_test, y1_train, y1_test = train_test_split(df1_x, df1_y, test_size = 0.1, random_state = 4)
x2_train, x2_test, y2_train, y2_test = train_test_split(df2_x, df2_y, test_size = 0.1, random_state = 4)

nn1 = MLPClassifier(activation = 'tanh', solver = 'lbfgs', hidden_layer_sizes = (100,200),random_state = 1)
nn2 = MLPClassifier(activation = 'tanh', solver = 'lbfgs', hidden_layer_sizes = (100,200),random_state = 1)

nn1.fit(x1_train, y1_train)
nn2.fit(x2_train, y2_train)
pred1 = nn1.predict(x1_test)
pred2 = nn2.predict(x1_test)

a1 = y1_test.values

a2 = y2_test.values

count1 = 0
for i in range(len(pred1)):
    if pred1[i] == a1[i]:
        count1 = count1 + 1
count2 = 0
for i in range(len(pred1)):
    if pred2[i] == a2[i]:
        count2 = count2 + 1
 
accuracy1 = float(count1)/len(pred1)
print str(accuracy1 * 100) + '%'

accuracy2 = float(count2)/len(pred2)
print str(accuracy2 * 100) + '%'    