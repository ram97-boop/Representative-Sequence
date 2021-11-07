# -*- coding: utf-8 -*- 

from Bio import pairwise2 as pw

class ScoreMatrix:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.matrix = self.createMatrix(self.cols)

    def createMatrix(self, cols):
        matrix = []
        for i in range(cols):
            matrix.append([])

        return matrix


def findScores(gene, otherSequences):
    '''
    Pairwise-aligns the sequences of gene with
    all of the sequences in otherSequences 
    and then calculates the scores of gene's
    sequences' alignments with them.

    Input:
    gene (list) = list of alternative sequences of gene.
    otherSequences (list) = list of all the other sequences.

    Output:
    scores = matrix of alignment scores from gene's
    sequences to all sequences in otherSequences.
    '''
    scores = ScoreMatrix(len(gene), len(otherSequences))
    seq_i = 0

    for seq1 in gene:
        for seq2 in otherSequences:
            alignment = pw.align.globalxx(seq1, seq2)
            scores.matrix[seq_i].append(alignment[0].score)

        seq_i+=1

    return scores.matrix

def findDistances(gene, otherSequences):
    '''
    Calculate the edit distances from gene's sequences
    to the sequences in otherSequences.

    Returns a ScoreMatrix containing the distances
    between gene's sequences and otherSequences sequences.
    '''
    distances = ScoreMatrix(len(gene), len(otherSequences))

    seq_i = 0 #The index of gene's sequences in the matrix distances.
    for seq1 in gene:
#        seq2_i = 0
        for seq2 in otherSequences:
            differences = 0
            
            i = 0
            while i < min([len(seq1), len(seq2)]): #This loop will iterate up to the length of the shorter sequence.
                if seq1[i] != seq2[i]:
                    differences += 1
#                    print(str(seq1[i])+ ' ' + str(seq2[i]) + ' ' + str(differences))

                i+=1
        
            differences += abs(len(seq1) - len(seq2)) #Add in the difference in length
            distances.matrix[seq_i].append(differences) #Store the distances between seq1 and all seq2's of otherSequences.
#            print('differences between ' +seq1 + ' and ' + seq2 +': ' + str(differences))

#            seq2_i+=1
#            print(seq2_i)

        seq_i += 1

    return distances.matrix

def getSequences(geneFile):
    '''
    Returns a list of the sequences in
    geneFile.
    '''
    gene = open(geneFile, 'r')
    line = gene.readline()
    sequences = [] #Will contain the sequences of gene.
    try:
        seq_i=0 #Will be used to index the list sequences.

        while line != '': #While we're not at the end of the file
            if line[0] == '>': #If we're at the identifier line of a sequence

                sequences.append('') #Add a placeholder for the sequence in the list sequences
                
                line = gene.readline() #Go to the next line, which is the start of the sequence

                while line != '\n': #While we're not at the end of the sequence

                    # Append the line (subsequence), without
                    # the '\n' character at the end, to the
                    # sequence in sequences[seq_i]
                    if line[-1] == '\n': #Note: Python sees '\n' as one character.
                        sequences[seq_i] += line[:-1]
                    else:
                        sequences[seq_i] += line

                    line = gene.readline()
                
                # line = '\n' after exiting the while loop
                # so we move to the next line which will
                # either start with '>' and is the identifier
                # line for the next sequence, or it will be
                # '' which is the end of the file.
                line = gene.readline()

                seq_i += 1
    except:
        print('Something went wrong')

    gene.close()
    return sequences

def getAllSeq(f):
    '''
    Returns a list of all the sequences in all
    the gene files listed in the file f (the
    gene files should be in the same
    directory as f).
    '''
    fileOfGenes = open(f, 'r')
    sequences = []

    geneFile = fileOfGenes.readline()
    while geneFile != '': #While we're not at the end of fileOfGenes
        sequences += getSequences(geneFile)
        geneFile = fileOfGenes.readline()

    fileOfGenes.close()
    return sequences

def getRepSeqFromScores(scoreMatrix):
    '''
    Returns the number (place) where the representative
    sequence is in its gene file. So if, for example,
    the 4th sequence is the representative in a file of
    5 sequences, then 4 will be returned.
    '''
    scoreSum = []
    for seqScores in scoreMatrix:
        # Sum all the scores of the sequence
        # and put it in scoreSum
        scoreSum.append(sum(seqScores))

    # Get the index of scoreSum with the maximum sum
    max_i = 0
    i = 0
    while i < len(scoreSum):
        if scoreSum[i] > scoreSum[max_i]:
            max_i = i
        i+=1

    return max_i

def getRepSeqFromDistances(distanceMatrix):
    '''
    Returns the number (place) where the representative
    sequence is in its gene file. So if, for example,
    the 4th sequence is the representative in a file of
    5 sequences, then 4 will be returned.
    '''
    distanceSum = []
    for seqDistances in distanceMatrix:
        # Sum all the distances of the sequence
        # and put it in distanceSum
        distanceSum.append(sum(seqDistances))

#    print(distanceSum)

    # Get the index of scoreSum with the minimum sum
    min_i = 0
    i = 0
    while i < len(distanceSum):
        if distanceSum[i] < distanceSum[min_i]:
            min_i = i
        i+=1

    return min_i

def main():
    '''
    Takes two files as input:
    file1: a gene containing sequences, which are its alternative transcripts.
    file2: all the sequences of all the other genes.

    Returns the number (placement) of the suggested representative sequence of the
    gene in file1.
    '''
    inputFiles = input() #Will take in a gene file and a file of all the other sequences.
    inputFiles = inputFiles.split() #Split the input into a list with ' ' as the delimiter.

#    gene = getSequences(inputFiles[0])
#    otherSequences = getAllSeq(inputFiles[1])

#    distances = findDistances(getSequences(inputFiles[0]), getSequences(inputFiles[1]))
#    repSeqNumber = getRepSeqFromDistances(distances)

    scores = findScores(getSequences(inputFiles[0]), getSequences(inputFiles[1]))
    repSeqNumber = getRepSeqFromScores(scores)

    print(str(repSeqNumber + 1)) # Print the number (placement) of the representative sequence in the gene file.

if __name__ == '__main__':
    main()

# Tests
#gene = getSequences('geneEx.fa')
#allSequences = getSequences('all_seq_no_gene.txt')
#scores = findScores(gene[0], gene[0])
#print(scores)
