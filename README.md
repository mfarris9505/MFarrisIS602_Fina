# MFarrisIS602_Final
## Requirements: 
To run the code as presented, Pybrain is necessary. To Install it's necessary to clone the github: The below code will do that:

$ git clone git://github.com/pybrain/pybrain.git
$ python setup.py install

As I was using Anaconda primarily, I was able to clone it in my prompt and install it in my ananconda directory.

## Code: 

The 3 main programs files are: 
Data_movie_Ratngs.py   USED FOR DATA EXTRACTION 
Pybrain_train.py       USED FOR PYBRAIN TRAINING
Pybrain_Test.py        USED FOR TESTING 


## Project: 

The Project is saved as a iPython notebook. Honestly because of the sheer length of training time for the pybrain neural network, I could not produce a function network. Theoretically it would require 11 days to train fully, my machine just couldn't handle that. In the future I will have to look up ways to speed up training of neural networks. 


## EXPLANATION OF CHANGE IN PROPOSAL/TIMELINESS

I must apologize here, my proposal was entirely different, I meant to use lyric data. However, I discovered that the Lyric wikia API I attempted to use (which I used previously for other projects), was shut down for licensing issues. This was the start of my many woes. I attempted for a couple weeks to scrap the lyric data, you can view some of my attempts in the Scrapped Folder (this is all UNUSED Code... which ammounts to ALOT). However, after researching Pybrain more, I realized that even if my attempts to scrap the lyrics succeeded (the didn't I just couldn't get scrapy to work for me), it would be useless as PyBrain only takes numeric data(at least I think? I tried finding some documentation of the latter, but couldn't). At that point, I switched to movie data, as this had a numeric "rating". At first I thought maybe I could do some semantic analysis on Movie Reviews, and input that into Pybrain. I learned a little about NLTK trainer, and was able to produce a bayesian classifer, but all it produced was a "pos" or "neg" response. This was just not enough info to train the Neural Network(Some of that code is also here, as reference, I am not going to explain it here in detail, as it was not utilized at all in the final project). At last, I found the dataset, and utilized that to train my neural network. Again, I must ardently apologize for the lack of insight. I suppose I could have prevented this with a more thorough investigation at the forefront of my project proposal.
