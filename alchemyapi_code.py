from alchemyapi import AlchemyAPI
from nltk.corpus.reader.plaintext import PlaintextCorpusReader


newcorpus = PlaintextCorpusReader('newcorpus/', '.*')


alchemyapi = AlchemyAPI()

for text in newcorpus:
    response = alchemyapi.sentiment("text",text)
    print "Sentiment: ", response["docSentiment"]["type"]