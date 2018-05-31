#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 19:14:36 2017

@author: sgkamal
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.cross_validation import train_test_split
data1 = pd.read_csv('dataa.csv')
data2 = pd.read_csv('donneg1.csv')
#print data.shape
df1_x = data1.iloc[:,:60]
#print df_x
df1_y = data1.iloc[:,60]
#print df_y
df2_x = data2.iloc[:,:60]
#print df_x
df2_y = data2.iloc[:,60]
x1_train, x1_test, y1_train, y1_test = train_test_split(df1_x, df1_y, test_size = 0.1, random_state = 4)
x2_train, x2_test, y2_train, y2_test = train_test_split(df2_x, df2_y, test_size = 0.1, random_state = 4)
nn1 = MLPClassifier(activation = 'logistic', solver = 'sgd', hidden_layer_sizes = (1,),random_state = 1)
nn2 = MLPClassifier(activation = 'logistic', solver = 'sgd', hidden_layer_sizes = (1,),random_state = 1)
nn1.fit(x1_train, y1_train)
nn2.fit(x2_train, y2_train)
pred1 = nn1.predict(x1_test)
pred2 = nn2.predict(x1_test)
a1 = y1_test.values
a1
a2 = y2_test.values

count = 0
for i in range(len(pred1)):
    if pred1[i] == a1[i]:
        count = count + 1
print sum(pred1 == pred2)
print len(pred1) 
print sum(pred1 == 0)
print sum(y1_test == 0)
print 'here'
count1 = 0
len(pred1)
accuracy = float(count)/len(pred1)
print str(accuracy * 100) + '%'
y1_test_array = np.array(y1_test)

y2_test_array = np.array(y2_test)

y1_train_array = np.array(y1_train)

y2_train_array = np.array(y2_train)

print sum(pred2 == y2_test_array)
print type(y1_test), type(y1_train), type(y2_test), type(y2_train)
for i in range(len(a2)):
    if y2_test_array[i] == a2[i]:
        count1 = count1 + 1
accuracy1 = float(count1)/len(a2)
print str(accuracy1 * 100) + '%'