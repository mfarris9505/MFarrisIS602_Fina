# -*- coding: utf-8 -*-
"""
Created on Sat May 28 00:14:03 2016

@author: Matts42
"""
import csv

import pybrain
import cPickle


f = open("subj.Steve+Rhodes")
text = csv.reader(f, delimiter = ",")
text = list(text)

f = open("rating.Steve+Rhodes")
rating = csv.reader(f, delimiter = ",")
rating = list(rating)
combined_1 = [rating,text]

f = open("subj.Steve+Rhodes")
text = csv.reader(f, delimiter = ",")
text = list(text)

f = open("rating.Steve+Rhodes")
rating = csv.reader(f, delimiter = ",")
rating = list(rating)
combined_1 = [rating,text]


f = open("subj.Steve+Rhodes")
text = csv.reader(f, delimiter = ",")
text = list(text)

f = open("rating.Steve+Rhodes")
rating = csv.reader(f, delimiter = ",")
rating = list(rating)
combined_1 = [rating,text]


f = open("subj.Steve+Rhodes")
text = csv.reader(f, delimiter = ",")
text = list(text)

f = open("rating.Steve+Rhodes")
rating = csv.reader(f, delimiter = ",")
rating = list(rating)
combined_1 = [rating,text]