from collections import defaultdict
from textblob import TextBlob
import pandas as pd
import numpy as np
import re
import nltk
try:
   import cPickle as pickle
except:
   import pickle

class StyleCreator(object):
    def __init__(self, path_to_text='styles/drizzy.txt'):
        self.path_to_text = path_to_text
        self.text = ''
        with open(path_to_text) as fh:
            self.text = fh.read()

        self.create_vocab()

    def create_vocab(self):
        '''
        INPUT: String of all text that you want to build the lexicon with.
        OUTPUT: A pickled object of the vocab_dict, that is the small heart of pyrapper and vocab_dict
        print vocab_dict [out] { 'JJ': ['big', 'huge', 'big', 'small', 'soft', 'rocky', 'big'], 'NN': ['dog', 'lawn', 'dog', 'dogs'] ... }
        '''

        # Convert text to unicode to aviod errors during the tagging process
        self.text = unicode(self.text, 'utf-8')

        vocab_dict = defaultdict(list)

        # blobify our string
        blob = TextBlob(self.text)

        # Create our (word, tag) tuple
        tagged =  blob.tags

        #  {'NN': [dog, cat, dog, human]}
        for word, tag in tagged:
            if len(word) > 1:
                vocab_dict[tag].append(word)

        filename_to_save_to = self.path_to_text[:-4] + '.pkl'
        pickle.dump( vocab_dict, open( filename_to_save_to, "wb" ) )
        return vocab_dict

StyleCreator()
