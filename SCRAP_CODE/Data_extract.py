# -*- coding: utf-8 -*-
"""
Created on Sat May 28 00:14:03 2016

@author: Matts42
"""
import csv
import numpy as np
import cPickle as pickle
from math import sqrt
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer


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
y_train = np.append(target_1,target_2)
y_train = np.append(y_train, target_3)


#PyBrain Training Initial Inputs:
output_model_file = 'model.pkl'

#This is the number of 
hidden_size = 100
epochs = 600

x_train = x_train.reshape(-1,1)
y_train = y_train.reshape(-1,1)

input_size = x_train.shape[1]
target_size = y_train.shape[1]

# prepare dataset

ds = SDS( input_size, target_size )
ds.setField( 'input', x_train )
ds.setField( 'target', y_train )

net = buildNetwork( input_size, hidden_size, target_size, bias = True )
trainer = BackpropTrainer( net,ds )

print "training for {} epochs...".format( epochs )

for i in range( epochs ):
	mse = trainer.train()
	rmse = sqrt( mse )
	print "training RMSE, epoch {}: {}".format( i + 1, rmse )
	
pickle.dump( net, open( output_model_file, 'wb' ))
