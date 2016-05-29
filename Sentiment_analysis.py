# -*- coding: utf-8 -*-
"""
Created on Sat May 28 22:04:26 2016

@author: Matts42
"""

from AlchemyAPI import AlchemyAPI
alchemyapi = AlchemyAPI()
from nltk.corpus.reader.plaintext import PlaintextCorpusReader


newcorpus = newcorpus = PlaintextCorpusReader('newcorpus/', '.*')