from collections import defaultdict
from textblob import TextBlob
import pandas as pd
import numpy as np
import re
import nltk


with open('drizzy.txt') as fh:
    text = fh.read()

#
# df = pd.read_csv('drake_importio.csv')
# list_of_lyrics = df['lyrics'].values


# text = ''
# for s in list_of_lyrics:
#     text += str(s)


def create_vocab(text):
    '''
    INPUT: String of all text that you want to build the lexicon with.
    OUTPUT: vocab_dict
    print vocab_dict [out] { 'JJ': ['big', 'huge', 'big', 'small', 'soft', 'rocky', 'big'], 'NN': ['dog', 'lawn', 'dog', 'dogs'] ... }
    '''

    # Convert text to unicode to aviod errors during the tagging process
    text = unicode(text, 'utf-8')

    vocab_dict = defaultdict(list)

    # blobify our string
    blob = TextBlob(text)

    # Create our (word, tag) tuple
    tagged =  blob.tags

    #  {'NN': [dog, cat, dog, human]}
    for word, tag in tagged:
        if len(word) > 1:
            vocab_dict[tag].append(word)

    return vocab_dict

vocab_dict = create_vocab(text)

def format_for_spew(the_string=''):

    the_string = unicode(the_string, 'utf-8')

    blob = TextBlob(the_string)

    lst_of_pos_tags = []

    for word, tag in blob.tags:
        lst_of_pos_tags.append(tag)

    return lst_of_pos_tags



def spew(lst_of_pos_tags):
    """
    INPUT:  A list of part-of-speech tags. ['JJ', 'NN', 'NNS', 'NN']
            the function format_for_spew does this with any string.
    OUTPUT:  A sentence of words that has the same flow of pos tags.
    """
    final_sentence = []
    for tag in lst_of_pos_tags:
        limit = len(vocab_dict[tag])
        # If for some reason there are no words associated with a tag, skip it.
        if not limit:
            continue
        # Chose a random interger index that is within the bounds of the
        # lenght of the limit
        random_choice = np.random.randint(0, limit)

        # Pluck out the random word.
        chosen_word = vocab_dict[tag][random_choice]

        # Appned it to the final sentnece.
        final_sentence.append(chosen_word)

    # Join the list of words into one senetece.
    final_sentence = ' '.join(final_sentence)

    return final_sentence


rap = "I dont like my chicks single, i like my girls in twos"

mystr = format_for_spew(rap)

print spew(mystr)

"""
var spewer = require('spewer');
var sentence = spewer.spew('JJ JJ NNS VBP RB');
console.log(sentence); // "colorless green ideas sleep furiously"
var sentence = spewer.spew('RB VBD IN PRP$ NN VBN JJR IN DT JJR NN');
console.log(sentence); // "sullen misty shoes lean reputedly"


sudo code for python spewer
===========================
get bunch of documents you want to build your spwerer from.
// lower and strip punt and shit, or not...
You can make them all one string, or they can be a list of docs.
Convert all the docs into text blobs.
then run textblob.tags.
that returns a list of tuples [('word', u'TAG'), ('cut','V')]
create a dictionary that the keys are all the tags (like 'V', or 'JJ')
the values is a list of every word that is that tag, with duplicates <-- duplcates are important.


vocab_dict = {
    'JJ': ['big', 'huge', 'big', 'small', 'soft', 'rocky', 'big'],
    'NN': ['dog', 'lawn', 'dog', 'dogs']
    }


then, in the spewer.spew(['JJ', 'NN'])

def spew(pos_key):
    limit = len(vocab[pos_key])
    pick = np.random.randint(0, limit)
    return vocab[pos_key][pick]

for
"""
