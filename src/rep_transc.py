# -*- coding: utf-8 -*- 

from Bio import pairwise2 as pw
import random

class ScoreMatrix:
    def __init__(self, cols):
        self.cols = cols
#        self.rows = rows
        self.matrix = self.createMatrix(self.cols)

    def createMatrix(self, cols):
        '''
        E.g. [[],[],[]] for a gene with 3 sequences (cols).
        '''
        matrix = []
        for i in range(cols):
            matrix.append([])

        return matrix


class Gene(ScoreMatrix):
    '''
    Inherits ScoreMatrix so it has the matrix attribute.
    
    sequences is a dictionary of the gene's alternative sequences.
    '''
    def __init__(self, name, sequences):
        self.name = name
        self.sequences = sequences
        super().__init__(len(sequences)) # Can get the matrix by GeneObject.matrix


def findScores(gene, otherSequences):
    '''
    Pairwise-aligns the sequences of gene with
    all of the sequences in otherSequences 
    and returns the alignment scores.

    Parameters
    ----------
    gene : list of strings.
        A list of the gene's alternative sequences.
    otherSequences : list of strings.
        A list of the alternative sequences of all the other genes.

    Returns
    -------
    scores.matrix : list of list of integers.
        Each inner list contains the alignment scores of one of gene's
        alternative sequences.
    '''
    scores = ScoreMatrix(len(gene))
    seq_i = 0 # Index of the 1st sequence of gene.

    for seq1 in gene:
        # print(seq_i)
        for seq2 in otherSequences:
            alignment = pw.align.globalms(seq1, seq2, 2, -1, -0.5, -0.1) #match = 2, mismatch = -1, opening gap = -0.5, extending gap = -0.1
            scores.matrix[seq_i].append(alignment[0].score)

        seq_i+=1 # Next sequence of gene

    return scores.matrix


def getSequences(geneFile):
    '''
    Returns a list of the sequences in the input file.

    Parameters
    ----------
    geneFile : string.
        The name of the file with the gene's alternative sequences.

    Returns
    -------
    sequences : list of strings.
        The alternative sequences of the gene in the input file.
    '''
    gene = open(geneFile, 'r')
    line = gene.readline()
    sequences = [] #Will contain the sequences of gene.
    try:
        seq_i=0 #Will be used to index the list called 'sequences'.

        while line != '': #While we're not at the end of the file
            if (line[0] == '>'): #If we're at the identifier line of a sequence

                # sequences.append('') #Add a placeholder element for the sequence in the list sequences
                sequences.append(line)
                
                line = gene.readline() #Go to the next line, which is the start of the sequence

                # while line != '\n': #While we're not at the end of the sequence
                while line[0] != '>': #While we're not at the beginning of the next sequence.

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
                # line = gene.readline()

                seq_i += 1
    except IndexError as e:
        # print(e)
        pass
    
    # Remove empty transcripts, i.e. a transcript ID with no transcript.
    i = 0
    while i < len(sequences):
        if sequences[i][-1] == '\n':
            sequences = sequences[:i] + sequences[i+1:]
        else:
            i+=1

    gene.close()
    return sequences


def getAllSeq(f):
    '''
    Returns a list of all the sequences in all
    the gene file names listed in the input file.

    Parameters
    ----------
    f : string.
        A file containing names of the gene files, where each gene file
        contains alternative sequences of a gene.

    Returns
    -------
    sequences : list of strings.
        A list of the sequences of all the gene files listed in f.
    '''
    geneFileNames = open(f, 'r')
    sequences = []

    geneFile = geneFileNames.readline()
    while geneFile != '': #While we're not at the end of geneFileNames
        sequences += getSequences(geneFile[:-1])
        geneFile = geneFileNames.readline()

    geneFileNames.close()
    return sequences

def getRepSeqFromScores(scoreMatrix):
    '''
    Get the index of a gene's alternative sequence that has the highest sum of
    pairwise alignment scores. This index corresponds the the sequence's
    placement in the gene's file. Note that the index is 0-indexed.

    Parameters
    ----------
    scoreMatrix : list of list of integers.
        Each inner list contains the alignment scores of one sequence of the
        gene.

    Returns
    -------
    max_i : integer.
        The index of the sequence with the highest sum of alignment scores.
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

def makeGeneDictionary(transcripts):
    '''
    Creates a dictionary for a gene, with the key : value pairs being the
    "sequence identifier" : "sequence" of the alternative sequences of the
    gene.

    Parameters
    ----------
    transcripts : list of strings.
        Each entry of the list must be e.g. ">cds_0_ggal\nATGCGA...",
        ">cds_0_btaus\nGAGTC", etc.

    Returns
    -------
    transcriptDict : dictionary
    '''
    transcriptDict = {}
    for transcript in transcripts:
        transcriptSplit = transcript.split('\n')
        transcriptDict[transcriptSplit[0]] = transcriptSplit[1] # Storing pairs of transcript ID : transcript.
        
    return transcriptDict

def fillScoreMatrices(geneList):
    '''
    Pairwisely aligns the alternative sequences of each gene with the sequences
    of all the other genes in the input list of genes. The scores are stored in
    the gene's score matrix. This is done for all the genes in the input list.
    After this function is done executing, all the genes should then have been
    aligned with the rest and the scores filled in their respective matrices.

    Parameters
    ----------
    geneList : list of Gene objects.

    Returns
    -------
    None.
    '''
    while len(geneList) > 1: #while there's more than 1 gene in geneList.
        gene = geneList[0]
        geneList = geneList[1:]
        print('Aligning and scoring.')
        
        for otherGene in geneList:
            scores = findScores(list(gene.sequences.values()), list(otherGene.sequences.values()))

            if len(gene.sequences) > 1: #if gene has more than 1 sequence.
                #store the scores in gene's matrix.
                for i in range(len(scores)):
                    gene.matrix[i] += scores[i]
                    
                    #store the scores in otherGene's matrix.
                    for j in range(len(scores[0])): #length of otherGene's matrix (number of sequences).
                        otherGene.matrix[j].append(scores[i][j])
                
            else: #if gene has only 1 sequence.
                #only store the scores in otherGene's matrix.
                for i in range(len(scores)):
                    for j in range(len(scores[0])):
                        otherGene.matrix[j].append(scores[i][j])

def findLongestTranscript(gene_transcripts):
    '''
    Find the index of the longest sequence of a gene. The index corresponds to
    the longest sequence's placement in the gene file. Note that the index is
    0-indexed.

    Parameters
    ----------
    gene_transcripts : dictionary
        The key : value pairs are the "sequence identifier" : "sequence" of
        the alternative sequences of the gene.

    Returns
    -------
    longest_id : integer
        The index of the longest sequence.
    '''
    transcripts = list(gene_transcripts.values())
    largestLength = 0
    longest_id = 0
    for i in range(len(transcripts)):
        if len(transcripts[i]) > largestLength:
            largestLength = len(transcripts[i])
            longest_id = i

    return longest_id

def chooseRandomTranscript(gene_transcripts):
    '''
    Returns the index of a randomly selected alternative sequence of a gene.

    Parameters
    ----------
    gene_transcripts : dictionary
        The key : value pairs are the "sequence identifier" : "sequence" of
        the alternative sequences of the gene.

    Returns
    -------
    An integer
    '''
    numberOfTranscripts = len(list(gene_transcripts.values()))
    return random.randint(0, numberOfTranscripts - 1) #randomly choose a number from 0 to (number of transcripts - 1).

def main():
    print("Selecting representative transcripts.")
    inputLine = input() # Will take in the name of the output file and then the input gene files.
    inputList = inputLine.split()
    geneFileList = inputList[1:] #e.g. ".../ggal.fa .../mdom.fa .../mmus.fa .../hsap.fa .../btaus.fa"
    
    geneList = [] #Will hold Gene objects for each gene-input-file.
    
    for gene in geneFileList:
        transcripts = makeGeneDictionary(getSequences(gene))
        geneList.append(Gene(gene, transcripts))
        
    fillScoreMatrices(geneList)

    representativeTranscript_id = []
    longestTranscript_id = []
    for gene in geneList:
        representativeTranscript_id.append(getRepSeqFromScores(gene.matrix))
        longestTranscript_id.append(findLongestTranscript(gene.sequences))
        #print(longestTranscript_id)
    

    transcriptFile = open(inputList[0], 'w')
    for i in range(len(geneList)):
        transcriptFile.write(list(geneList[i].sequences.keys())[representativeTranscript_id[i]] + "\n")
        transcriptFile.write(list(geneList[i].sequences.values())[representativeTranscript_id[i]] + "\n")
    
    transcriptFile.close()
        
def main2():
    print("Finding longest transcripts.")
    inputLine = input()
    inputList = inputLine.split()
    geneFileList = inputList[1:]
    geneList = []

    for gene in geneFileList:
        transcripts = makeGeneDictionary(getSequences(gene))
        geneList.append(Gene(gene, transcripts))

    longestTranscripts_ids = []
    for gene in geneList:
        longestTranscripts_ids.append(findLongestTranscript(gene.sequences))

    longestTranscriptFile = open(inputList[0], 'w')
    for i in range(len(geneList)):
        longestTranscriptFile.write(list(geneList[i].sequences.keys())[longestTranscripts_ids[i]] + "\n")
        longestTranscriptFile.write(list(geneList[i].sequences.values())[longestTranscripts_ids[i]] + "\n")
        
    longestTranscriptFile.close()
        
def main3():
    print("Randomly choosing transcripts.")
    inputLine = input()
    inputList = inputLine.split()
    geneFileList = inputList[1:]
    geneList = []
    
    for gene in geneFileList:
        transcripts = makeGeneDictionary(getSequences(gene))
        geneList.append(Gene(gene, transcripts))
        
    randomTranscripts_ids = []
    for gene in geneList:
        randomTranscripts_ids.append(chooseRandomTranscript(gene.sequences))
        
    randomTranscriptFile = open(inputList[0], 'w')
    for i in range(len(geneList)):
        randomTranscriptFile.write(list(geneList[i].sequences.keys())[randomTranscripts_ids[i]] + "\n")
        randomTranscriptFile.write(list(geneList[i].sequences.values())[randomTranscripts_ids[i]] + "\n")
        
    randomTranscriptFile.close()

# if __name__ == '__main__':
    # main()
    #main2()
    #main3()


##### Tests

#gene = getSequences('geneEx.fa')
#allSequences = getSequences('all_seq_no_gene.txt')
#scores = findScores(gene[0], gene[0])
#print(scores)

# Gene class #
#geneSequences = getSequences('geneEx.fa')
#geneTest = Gene(0, geneSequences)
#print(geneTest.matrix)
