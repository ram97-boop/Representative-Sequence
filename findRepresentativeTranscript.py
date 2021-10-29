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

def getSequences(f, gene_i):
    '''
    Input:
    f (str) = file name.
    gene_i (int) = the index of the gene that will
    be the parameter 'gene' in findScores().

    Output:
    gene (list of str) = sequences of gene with the
    index i in the file f.
    otherSequences (list of str) = sequences of the
    rest of the genes in f.
    '''

def arrangeGenes(f, output_f):
    '''
    Input:
    '''
