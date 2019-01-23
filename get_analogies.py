"""Get analogies from embeddings"""

import numpy as np
from scipy.spatial.distance import cdist
import sys

wv = np.loadtxt(sys.argv[1]+'.wordvec')
words = open(sys.argv[1]+'.words').read().split()
wordmap = {word: i for i, word in enumerate(words)}

while True:
    print 'worda - wordb + wordc = ?'
    worda = raw_input('Enter worda: ')
    if worda not in wordmap:
        print 'Word not in vocabulary'
        continue
    wordb = raw_input('Enter wordb: ')
    if wordb not in wordmap:
        print 'Word not in vocabulary'
        continue
    wordc = raw_input('Enter wordc: ')
    if wordc not in wordmap:
        print 'Word not in vocabulary'
        continue
    result = wv[wordmap[worda]]-wv[wordmap[wordb]]+wv[wordmap[wordc]]
    cd = cdist(result.reshape((1, result.size)), wv)
    closest = np.argsort(cd[0])[1:13]
    for i in closest:
        if words[i] not in [worda, wordb, wordc]:
            print words[i],
    print
