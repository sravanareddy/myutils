#!/bin/bash

# separate .word2vec file into .wordvec and .words files
FILENAME=$1.word2vec

awk -F' ' '{print $1}' $FILENAME | tail -n+2 > $1.words
awk -F' ' '{for (i = 2; i <= NF; i++) printf $i " "; print ""}' $FILENAME | tail -n+2 > $1.wordvec
