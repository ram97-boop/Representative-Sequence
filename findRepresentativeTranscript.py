# -*- coding: utf-8 -*- 

from Bio import pairwise2 as pw
import numpy as np

class DistanceMatrix:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.matrix = self.createMatrix(self.cols)
        

    def createMatrix(self, cols):
        matrix = []
        for i in range(cols):
            matrix.append([])

        return np.array(matrix, dtype=int)



def findDistances(seq, other_sequences):
    '''
    Pairwise-aligns the sequence seq with
    all the sequences in the other_sequences 
    and then calculates the distances from
    seq to all of them.

    Output:
    distances (list of distances from
    seq to all sequences in other_sequences)
    '''
    
