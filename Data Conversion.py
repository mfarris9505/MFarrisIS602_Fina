# -*- coding: utf-8 -*-
"""
Created on Sat May 28 00:14:03 2016

@author: Matts42
"""
import csv
import numpy as np

from nltk.corpus import PlaintextCorpusReader

#Extracting the Raw data and loading it to Numpy Arrays
f = open("data_in/subj.Steve+Rhodes")
text = csv.reader(f, delimiter = ",")
text = list(text)

f = open("data_in/rating.Steve+Rhodes")
rating = csv.reader(f, delimiter = ",")
rating = list(rating)

input_1 = np.array(text)
target_1 = np.array(rating)

f = open("data_in/subj.Scott+Renshaw")
text = csv.reader(f, delimiter = ",")
text = list(text)

f = open("data_in/rating.Scott+Renshaw")
rating = csv.reader(f, delimiter = ",")
rating = list(rating)

input_2 = np.array(text)
target_2 = np.array(rating)

f = open("data_in/subj.James+Berardinelli")
text = csv.reader(f, delimiter = ",")
text = list(text)

f = open("data_in/rating.James+Berardinelli")
rating = csv.reader(f, delimiter = ",")
rating = list(rating)

input_3 = np.array(text)
target_3 = np.array(rating)

f = open("data_in/subj.Dennis+Schwartz")
text = csv.reader(f, delimiter = ",")
text = list(text)

f = open("data_in/rating.Dennis+Schwartz")
rating = csv.reader(f, delimiter = ",")
rating = list(rating)

input_4 = np.array(text)
target_4 = np.array(rating)


#Forcing to Float
target_1 = target_1.astype(float)
target_2 = target_2.astype(float)
target_3 = target_3.astype(float)


#Removing some "Excess Data" Discussion to follow
target_3 = np.delete(target_3, 1306)
target_1 = np.delete(target_1, 1769)
target_1 = np.delete(target_1, 100)


#Combining datasets
x_train = np.append(input_1,input_2)
x_train = np.append(x_train, input_3)
x_train = np.append(x_train, input_4)
y_train = np.append(target_1,target_2)
y_train = np.append(y_train, target_3)

corpusdir = "newcorpus/"
filename = 0
for text in x_train:
    filename+=1
    with open(corpusdir+str(filename)+'.txt','w') as fout:
        print>>fout, text

    