# -*- coding: utf-8 -*-

import numpy as np
import rep_transc

def makeMsaDictionary(msa):
    '''
    Input:
    msa: the MSA file.

    Output:
    A dictionary of the sequences in the MSA, with a key
    being the identifier of the sequences and the value being
    the sequence itself.
    '''
    return rep_transc.makeGeneDictionary(rep_transc.getSequences(msa))

def scorePair(seq1, seq2):
    '''
    Input:
    seq1: a sequence in the MSA.

    seq2: another sequence in the MSA.

    Output:
    The score (int) between these two sequences of the MSA.
    '''
    match = 3
    mismatch = -2
    indel = -1
    
    score = 0
    length = len(seq1)
    for i in range(length):
        if seq1[i] == seq2[i]:
            score += match
        elif (seq1[i] == "-") or (seq2[i] == "-"):
            score += indel
        else:
            score += mismatch
            
    return score

def main():

    #User input must be the output file name and then the input MSA file.
    inputLine = input()
    inputList = inputLine.split()
    sequenceDictionary = makeMsaDictionary(inputList[1])

    #Create a 5x5 matrix full of zeros.
    matrix = np.zeros((5,5))
