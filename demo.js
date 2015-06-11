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
