import numpy as np
import sys

vecfile = sys.argv[1]
threshold = int(sys.argv[2])

vectors = np.loadtxt(vecfile+'.wordvec')
unkvec = np.mean(vectors[threshold:], axis=0)

vocab = open(vecfile+'.words').readlines()[:threshold]

vocab.insert(0, 'UNK\n')
vectors = np.vstack((unkvec, vectors[:threshold]))

np.savetxt(vecfile+'.unk'+str(threshold)+'.wordvec', vectors)
with open(vecfile+'.unk'+str(threshold)+'.words', 'w') as o:
    o.write(''.join(vocab))
