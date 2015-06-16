from collections import defaultdict, deque
from textblob import TextBlob
import numpy as np
import re

try:
   import cPickle as pickle
except:
   import pickle

class StyleCreator(object):
    def __init__(self, path_to_text='styles/default.txt'):
        '''
        INPUT:  A text file that is the text you want to create your rapper's
        vocabulary from.

        OUTPUT:  It will save the approipate dictionarys it uses to then create
        raps as pickled dictionarys.
        '''

        self.path_to_text = path_to_text
        self.text = ''
        with open(path_to_text) as fh:
            self.text = fh.read()

        self.pos_dict = self.create_pos_dict()
        self.mcmc_dict = self.create_mcmc_dict()
        self.mcmc_dict_unigram = self.create_mcmc_dict_unigram()

    def create_pos_dict(self):
        '''
        INPUT: String of all text that you want to build the lexicon with.
        OUTPUT: A pickled object of the pos_dict, that is the small heart of pyrapper
        print pos_dict [out] { 'JJ': ['big', 'huge', 'big', 'small', 'soft', 'rocky', 'big'], 'NN': ['dog', 'lawn', 'dog', 'dogs'] ... }
        '''

        # Convert text to unicode to aviod errors during the tagging process
        self.text = unicode(self.text, 'utf-8')

        pos_dict = defaultdict(list)

        # blobify our string
        blob = TextBlob(self.text)

        # Create our (word, tag) tuple
        tagged =  blob.tags

        #  {'NN': [dog, cat, dog, human]}
        for word, tag in tagged:
            if len(word) >= 1: # <--- if not an empty string
                pos_dict[tag].append(word)

        filename_to_save_to = self.path_to_text[:-4] + '_pos_dict.pkl'
        pickle.dump( pos_dict, open( filename_to_save_to, "wb" ) )
        print "saved %s " % filename_to_save_to

        return pos_dict

    def create_mcmc_dict_unigram(self):
        self.text = self.text.encode('ascii', 'ignore')

        blob = TextBlob(self.text)
        blob = blob.lower()


        mcmc_dict = defaultdict(list)

        words_shifted_zero = blob.split(' ')
        words_shifted_one = blob.split(' ')

        words_shifted_zero = deque(words_shifted_zero)
        words_shifted_one = deque(words_shifted_one)

        # words_shifted_zero.rotate(0)
        words_shifted_one.rotate(-1)


        for zero, one in zip(words_shifted_zero, words_shifted_one):
            mcmc_dict[zero].append(one)

        filename_to_save_to = self.path_to_text[:-4] + '_mcmc_dict_unigram.pkl'
        print "saved %s " % filename_to_save_to
        pickle.dump( mcmc_dict, open( filename_to_save_to, "wb" ) )

    def create_mcmc_dict(self):
        self.text = self.text.encode('ascii', 'ignore')

        blob = TextBlob(self.text)
        blob = blob.lower()

        mcmc_dict = defaultdict(list)

        words_shifted_zero = blob.split(' ')
        words_shifted_one = blob.split(' ')
        words_shifted_two = blob.split(' ')

        words_shifted_zero = deque(words_shifted_zero)
        words_shifted_one = deque(words_shifted_one)
        words_shifted_two = deque(words_shifted_two)
        # words_shifted_zero.rotate(0)
        words_shifted_one.rotate(-1)
        words_shifted_two.rotate(-2)

        for zero, one, two in zip(words_shifted_zero, words_shifted_one, words_shifted_two):
            mcmc_dict[(zero, one)].append(two)

        filename_to_save_to = self.path_to_text[:-4] + '_mcmc_dict.pkl'
        pickle.dump( mcmc_dict, open( filename_to_save_to, "wb" ) )

        print "saved %s " % filename_to_save_to
        return mcmc_dict

#
sc = StyleCreator()
