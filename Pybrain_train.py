# -*- coding: utf-8 -*-
"""
Training the Neural Network 

As the Documentation from Pybrain was very limited a lot 
of the code was modelled off  of: 

http://fastml.com/pybrain-a-simple-neural-networks-library-in-python/

"""

import cPickle as pickle
import numpy as np 
import csv
from sklearn.cross_validation import train_test_split
from math import sqrt
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.customxml.networkwriter import NetworkWriter



#Load Data
f = open("total_pd.csv")
load = csv.reader(f, delimiter = ",")
total = list(load)

total.pop(0)
total = np.array(total)
total = total.astype(int)

train, test = train_test_split(total, test_size = 0.2)

#Save Split
np.savetxt("train3.csv", train)
np.savetxt("test3.csv", test)

#Initial Variables
hidden_size = 100
epochs = 350
output = "model3.pk1"

#Training and Target
x_train = train[:,1:-3]
y_train = train [:,-3:]

input_size = x_train.shape[1]
target_size = y_train.shape[1]


#Building the Neural Network
ds = SDS(input_size,target_size)
ds.setField('input',x_train)
ds.setField('target',y_train)

net = buildNetwork(input_size,hidden_size,target_size, bias=True)
trainer = BackpropTrainer(net,ds)


print "training for {} epochs...".format( epochs )

for i in range( epochs ):
	mse = trainer.train()
	rmse = sqrt( mse )
	print "training RMSE, epoch {}: {}".format( i + 1, rmse )
	
pickle.dump(net, open( output, 'wb' ))
NetworkWriter.writeToFile(net, 'network3.xml')


