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
        seq_i=0
        # While we're not at the end of the file
        while line != '':
            # If we're at the identifier line of a sequence
            if line[0] == '>':

                # Add a placeholder for the sequence in
                # the sequence list
                sequences.append('')

                # Go to the next line, which is the start
                # of the sequence
                line = gene.readline()

                # While we're not at the end of the sequence
                while line != '\n':

                    # Append the line of subsequence without
                    # the '\n' at the end
                    if line[-1] == '\n':
                        sequences[seq_i] += line[:-1]
                    else:
                        sequences[seq_i] += line

                    line = gene.readline()
                
                # line = '\n' so we move to next line
                # which will start with '>'
                line = gene.readline()

                seq_i += 1
    except:
        print('Something went wrong')

    return sequences
