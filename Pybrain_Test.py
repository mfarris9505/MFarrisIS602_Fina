# -*- coding: utf-8 -*-
"""
Testing the Neural Network against the test file

"""

import numpy as np 
import cPickle as pickle
from math import sqrt
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from sklearn.metrics import mean_squared_error as MSE

#Loading data

test = np.loadtxt("data_out/test3.csv")
test = test.astype(int)
net = pickle.load(open("data_out/model3.pk1","rb"))


#Variables
x_test = test[:,1:-3]
y_test = test[:,-3:]
y_test_pred = np.zeros(y_test.shape)

input_size = x_test.shape[1]
target_size = y_test.shape[1]

assert(net.indim == input_size)
assert(net.outdim == target_size)

ds = SDS(input_size,target_size)
ds.setField('input',x_test)
ds.setField('target',y_test_pred)


p = net.activateOnDataset(ds)

mse = MSE(y_test, p)
rmse = sqrt(mse)

print "testing RMSE:", rmse

np.savetxt("pred", p, fmt = '%.6f')
