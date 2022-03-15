from rep_transc import getSequences, makeGeneDictionary

def makeAlignmentDictionary(f):
    '''
    Input:
        f (str): the MSA file.

    Output:
        alignmentDictionary (dict): a dictionary whose values
        are the sequences in the MSA, and whose keys are the
        sequence IDs of the sequences.
    '''
    sequenceList = getSequences(f)
    alignmentDictionary = makeGeneDictionary(sequenceList)
    return alignmentDictionary

def countIndelsMismatches(alignmentDictionary):
    '''
    '''
    sequenceList = list(alignmentDictionary.values())
    count = 0
    for i in range(len(sequenceList[0])): # i.e. for each column of the alignment.
        characterList = []
        isIndelMismatch = False
        for sequence in sequenceList: # for each sequence in the alignment.
            if sequence[i] == "-": # if this column of the sequence is an indel.
                isIndelMismatch = True
                break
            
            characterList.append(sequence[i])
        
        if not isIndelMismatch: # if there is no indel in this column of the alignment.
            character1 = characterList[0]
            for char in characterList[1:]:
                if character1 != char: # mismatch.
                    isIndelMismatch = True
                    break
                
                character1 = char

        if isIndelMismatch:
            count += 1

    return count


def main():
    inputLine = input() # Will take in the respective MSA files of the
                        # representative transcripts, longest transcripts
                        # and the randomly chosen transcripts in that order.

    inputList = inputLine.split()
    outputFile = open('indels_mismatches.txt', 'w')

    for msa in inputList:
        alignmentDictionary = makeAlignmentDictionary(msa)
        indelsMismatches = countIndelsMismatches(alignmentDictionary)
        pass
