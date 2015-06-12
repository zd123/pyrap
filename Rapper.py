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

class Rapper(object):
    def __init__(self, style='styles/default_default.pkl'):
        self.vocab_dict = pickle.load(open( "styles/defualt_style.pkl", "rb" ) )
        print 'Chyeahhh boiiiii!, welcome to pyrapper'

    def format_for_spew(self, the_string=''):
        the_string = unicode(the_string, 'utf-8')
        blob = TextBlob(the_string)

        lst_of_pos_tags = []

        for word, tag in blob.tags:
            lst_of_pos_tags.append(tag)

        return lst_of_pos_tags

    def spit(self, sentnece='We rollin, the hatin'):

        lst_of_pos_tags = self.format_for_spew(sentnece)

        final_sentence = []

        for tag in lst_of_pos_tags:
            limit = len(self.vocab_dict[tag])
            # If for some reason there are no words associated with a tag, skip it.
            if not limit:
                continue
            # Chose a random interger index that is within the bounds of the
            # lenght of the limit
            random_choice = np.random.randint(0, limit)

            # Pluck out the random word.
            chosen_word = self.vocab_dict[tag][random_choice]

            # Appned it to the final sentnece.
            final_sentence.append(chosen_word)

        # Join the list of words into one senetece.
        final_sentence = ' '.join(final_sentence)

        return final_sentence


rapper = Rapper()
print rapper.spit('hey ladies ladies you wanna ride in my Mercades??')
