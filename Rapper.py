from collections import defaultdict, deque
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
    def __init__(self, style='default'):
        '''
        INPUT:  The type of style stil you want the rapper to be.
        The files should be in the style folder.
        '''
        self.pos_dict = pickle.load(open( 'styles/' + style + '_pos_dict.pkl', "rb" ) )
        self.mcmc_dict = pickle.load(open( 'styles/' + style + '_mcmc_dict.pkl', "rb" ) )
        self.mcmc_dict_unigram = pickle.load(open( 'styles/' + style + '_mcmc_dict_unigram.pkl', "rb" ) )
        print 'Chyeahhh boiiiii!, welcome to pyrapper'

    def format_for_pos_spit(self, the_string=''):
        the_string = unicode(the_string, 'utf-8')
        blob = TextBlob(the_string)

        lst_of_pos_tags = []

        for word, tag in blob.tags:
            lst_of_pos_tags.append(tag)

        return lst_of_pos_tags


    def pos_spit(self, sentnece='We rollin, they hatin'):
        lst_of_pos_tags = self.format_for_pos_spit(sentnece)
        final_sentence = []

        for tag in lst_of_pos_tags:
            limit = len(self.pos_dict[tag])
            # If for some reason there are no words associated with a tag, skip it.
            if not limit:
                continue
            # Chose a random interger index that is within the bounds of the
            # lenght of the limit
            random_choice = np.random.randint(0, limit)

            # Pluck out the random word.
            chosen_word = self.pos_dict[tag][random_choice]

            # Appned it to the final sentnece.
            final_sentence.append(chosen_word)

        # Join the list of words into one senetece.
        final_sentence = ' '.join(final_sentence)

        return final_sentence


    def format_for_mcmc_unigram_spit(self, the_string=''):
        the_string = unicode(the_string, 'utf-8')
        words_shifted_zero = the_string.split(' ')
        words_shifted_one = the_string.split(' ')

        words_shifted_zero = deque(words_shifted_zero)
        words_shifted_one = deque(words_shifted_one)

        # words_shifted_zero.rotate(0)
        words_shifted_one.rotate(-1)
        lst_of_unigram_tuples = []

        for zero, one in zip(words_shifted_zero, words_shifted_one):
            lst_of_unigram_tuples.append((zero))
        return lst_of_unigram_tuples



    def format_for_mcmc_spit(self, the_string=''):
        the_string = unicode(the_string, 'utf-8')
        words_shifted_zero = the_string.split(' ')
        words_shifted_one = the_string.split(' ')

        words_shifted_zero = deque(words_shifted_zero)
        words_shifted_one = deque(words_shifted_one)

        # words_shifted_zero.rotate(0)
        words_shifted_one.rotate(-1)
        lst_of_bigram_tuples = []

        for zero, one in zip(words_shifted_zero, words_shifted_one):
            lst_of_bigram_tuples.append( (zero,one) )
        return lst_of_bigram_tuples


    def mcmc_unigram_spit(self, sentence='We rollin, they hatin'):
        lst_of_unigram_tuples = self.format_for_mcmc_unigram_spit(sentence)
        final_sentence = []

        for tag in lst_of_unigram_tuples:
            limit = len(self.mcmc_dict_unigram[tag])


            # If for some reason there are no words associated with a tag, skip it.
            if not limit:
                continue

            if limit <= 3:
                continue
            # Chose a random interger index that is within the bounds of the
            # lenght of the limit
            random_choice = np.random.randint(0, limit)

            # Pluck out the random word.
            chosen_word = self.mcmc_dict_unigram[tag][random_choice]

            if not chosen_word:
                continue

            # Appned it to the final sentnece.
            final_sentence.append(chosen_word)

        final_sentence = ' '.join(final_sentence)

        return final_sentence


    def mcmc_spit(self, sentence='We rollin, they hatin'):
        lst_of_bigram_tuples = self.format_for_mcmc_spit(sentence)
        final_sentence = []

        for tag in lst_of_bigram_tuples:
            limit = len(self.mcmc_dict[tag])

            # If for some reason there are no words associated with a tag, skip it.
            if not limit:
                continue

            # Chose a random interger index that is within the bounds of the
            # lenght of the limit
            random_choice = np.random.randint(0, limit)

            # Pluck out the random word.
            chosen_word = self.mcmc_dict[tag][random_choice]

            if not chosen_word:
                continue

            # Appned it to the final sentnece.
            final_sentence.append(chosen_word)

        final_sentence = ' '.join(final_sentence)

        return final_sentence

    def spit(self, sentence='we rollin they hatin cause we ridin dirty'):
        print "PART OF SPEECH BASED RAP: ",self.pos_spit(sentence), '\n\n'
        print "BI-GRAM MCMC BASED RAP: ", self.mcmc_spit(sentence), '\n\n'
        print "UNI-GRAM MCMC BASED RAP: ",self.mcmc_unigram_spit(sentence), '\n\n'


# rp = Rapper(style='the_bible')
# original = "grace of our Lord Jesus Christ be with you all. Amen."
# print original
# print '-'*80
# print "\noriginal above, computer mcmc rap below"
# print '-'*80
# print rp.mcmc_spit(original)
# print '-'*80
# print "\n pos_rap below"
# print rp.pos_spit(original)
# print "\n unigram mcmc_below"
# print rp.mcmc_unigram_spit(original)
