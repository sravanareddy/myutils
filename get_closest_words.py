"""Get closest words in embeddings"""

import numpy as np
from scipy.spatial.distance import cdist
import sys

wv = np.loadtxt(sys.argv[1]+'.wordvec')
words = open(sys.argv[1]+'.words').read().split()
wordmap = {word: i for i, word in enumerate(words)}
metric = 'euclidean' if len(sys.argv)==2 else sys.argv[2]

while True:
    refword = raw_input('Enter a word: ')
    if refword not in wordmap:
        print 'Word not in vocabulary'
        continue
    cd = cdist(wv[wordmap[refword]:wordmap[refword]+1], wv, metric)
    closest = np.argsort(cd[0])[1:103]
    for i in closest:
        print words[i],
    print
