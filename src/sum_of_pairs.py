# -*- coding: utf-8 -*-

# import numpy as np
import rep_transc

def makeMsaDictionary(msa):
    '''
    Make a dictionary of the input MSA. The keys will be the MSA's sequence
    identifiers and the values will be the sequences themselves.

    Parameters
    ----------
    msa : string.
        name of the MSA file.

    Returns
    -------
    dictionary.
    '''
    return rep_transc.makeGeneDictionary(rep_transc.getSequences(msa))

def scorePair(seq1, seq2):
    '''
    Score a pair of sequences from an MSA using the sum-of-pairs method.

    Parameters
    ----------
    seq1 : string.
        
    seq2 : string.

    Returns
    -------
    score : integer.
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
    #inputLine = input("Enter the output file name and then the input MSA file: ")
    inputLine = input()
    #inputList = inputLine.split()
    #sequenceDictionary = makeMsaDictionary(inputList[1])
    sequenceDictionary = makeMsaDictionary(inputLine)
    sequenceList = list(sequenceDictionary.values())
    
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
