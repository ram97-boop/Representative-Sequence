# -*- coding: utf-8 -*- 

from Bio import pairwise2 as pw

class DistanceMatrix:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.matrix = self.createMatrix(self.cols)
        

    def createMatrix(self, cols):
        matrix = []
        for i in range(cols):
            matrix.append([])

        return matrix



def findScores(gene, other_sequences):
    '''
    Pairwise-aligns the sequences of gene with
    all of the sequences in other_sequences 
    and then calculates the scores of gene's
    sequences' alignments with them.

    Output:
    scores = matrix of alignment scores from gene's
    sequences to all sequences in other_sequences.
    '''
    scores = DistanceMatrix(len(gene), len(other_sequences))
    seq_i = 0

    for seq1 in gene:
        for seq2 in other_sequences:
            alignment = pw.align.globalxx(seq1, seq2)
            scores.matrix[seq_i].append(alignment[0].score)

        seq_i+=1

    return scores
