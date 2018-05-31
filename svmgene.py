#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 17:59:28 2017

@author: sgkamal
"""


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.cross_validation import train_test_split
from sklearn import svm
data1 = pd.read_csv('accneg.csv')
data2 = pd.read_csv('donneg.csv')
#print data.shape
df1_x = data1.iloc[:,:10]
#print df_x
df1_y = data1.iloc[:,10]
#print df_y
df2_x = data2.iloc[:,:10]
#print df_x
df2_y = data2.iloc[:,10]
x1_train, x1_test, y1_train, y1_test = train_test_split(df1_x, df1_y, test_size = 0.1, random_state = 4)
x2_train, x2_test, y2_train, y2_test = train_test_split(df2_x, df2_y, test_size = 0.1, random_state = 4)
nn1 = MLPClassifier(activation = 'logistic', solver = 'sgd', hidden_layer_sizes = (1,),random_state = 1)
nn2 = MLPClassifier(activation = 'logistic', solver = 'sgd', hidden_layer_sizes = (1,),random_state = 1)
nn1.fit(x1_train, y1_train)
nn2.fit(x2_train, y2_train)
pred1 = nn1.predict(x1_test)
pred2 = nn2.predict(x2_test)
a1 = y1_test.values
a1
a2 = y2_test.values

clf = svm.SVC(kernel = 'linear')
clf.fit(x1_train, y1_train)
a4 = clf.predict(x1_test)
count = 0
count1 = 0
for i in range(len(pred1)):
    if pred1[i] == a1[i]:
        count = count + 1
some = np.array(y1_test)
print type(some)
for i in range(len(a4)):
    if a4[i] == some[i]:
        count1 += 1
print len(a4) == len(y1_test)
print type(a4), type(y1_test)
#print y1_test
count
len(pred1)
accuracy = float(count)/len(pred1)
print str(accuracy * 100) + '%'
accuracy1 = float(count1)/len(a4)
print str(accuracy1 * 100) + '%'