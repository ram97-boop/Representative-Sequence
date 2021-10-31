# -*- coding: utf-8 -*- 

from Bio import pairwise2 as pw

class ScoreMatrix:
    def __init__(self, gene, cols, rows):
        self.gene = gene
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

    return scores

def getSequences(geneFile):
    '''
    Returns a list of the sequences in
    geneFile.
    '''
    gene = open(geneFile, 'r')
    line = gene.readline()
    sequences = [] # Will contain the sequences of gene.
    try:
        seq_i=0 # Will be used to index the list sequences.

        # While we're not at the end of the file
        while line != '':
            # If we're at the identifier line of a sequence
            if line[0] == '>':
                # Add a placeholder for the sequence in
                # the list sequences
                sequences.append('')

                # Go to the next line, which is the start
                # of the sequence
                line = gene.readline()

                # While we're not at the end of the sequence
                while line != '\n':
                    # Append the line (subsequence) without
                    # the '\n' character at the end to the
                    # sequence in sequences[seq_i]
                    if line[-1] == '\n':
                        sequences[seq_i] += line[:-1]
                    else:
                        sequences[seq_i] += line

                    line = gene.readline()
                
                # line = '\n' so we move to the next line
                # which will start with '>' and is the
                # identifier line for the next sequence
                line = gene.readline()

                seq_i += 1
    except:
        print('Something went wrong')

    return sequences

def getAllSeq(f):
    '''
    Returns a list of all the sequences in all
    the gene files with their file names in f.
    '''
    fileOfGenes = open(f, 'r')
    sequences = []

    geneFile = fileOfGenes.readline()
    while geneFile != '': #While we're not at the end of fileOfGenes
        sequences += getSequences(geneFile)

    return sequences

def getRepSeq(scoreMatrix):
    '''
    Returns the number (place) where the representative
    sequence is in its gene file.
    '''
    scoreSum = []
    for seqScores in scoreMatrix:
        # Sum the all the scores of the sequence
        # and put it in scoreSum
        scoreSum.append(sum(seqScores))

    # Get the index of scoreSum with the maximum sum
    max_i = 0
    i = 0
    while i < len(scoreSum):
        if scoreSum[i] > scoreSum[max_i]:
            max_i = i
        i+=1
