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
    for i in range(len(seq1)):
        if (seq1[i] == seq2[i]):
            if seq1[i] == "-": #If this column is a gap with no protein residues in either sequence.
                pass
            else:
                score += match
                
        else: #If the sequence residues are different at this column.
            if (seq1[i] == "-") or (seq2[i] == "-"):
                score += indel
            else: #If neither sequence has an indel character.
                score += mismatch
            
    return score

def main():

    #User input must be the output file name and then the input MSA file.
    inputLine = input()
    inputList = inputLine.split()
    sequenceDictionary = makeMsaDictionary(inputList[1])
    sequenceList = list(sequenceDictionary.values())

    #Create a 5x5 matrix full of zeros.
    # matrix = np.zeros((5,5))
    
    sumOfPairs = 0

    for i in range(len(sequenceList) - 1):
        j = i + 1
        while j < len(sequenceList):
            # matrix[i][j] = scorePair(sequenceList[i], sequenceList[j])
            sumOfPairs += scorePair(sequenceList[i], sequenceList[j])
            j += 1
            
    print(sumOfPairs)
    
if __name__ == "__main__":
    main()
            
    