# -*- coding: utf-8 -*- 

from Bio import pairwise2 as pw

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
    and then calculates the scores of gene's
    sequences' alignments with them.

    Input:
    gene (list) = list of alternative sequences of gene.
    otherSequences (list) = list of all the other sequences.

    Output:
    scores.matrix (list) = matrix of alignment scores from gene's
    sequences to all sequences in otherSequences.
    '''
    scores = ScoreMatrix(len(gene))
    seq_i = 0 # Index of the 1st sequence of gene.

    for seq1 in gene:
        for seq2 in otherSequences:
            alignment = pw.align.globalxx(seq1, seq2)
            scores.matrix[seq_i].append(alignment[0].score)

        seq_i+=1 # Next sequence of gene

    return scores.matrix


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

    gene.close()
    return sequences


def getAllSeq(f):
    '''
    Returns a list of all the sequences in all
    the gene files listed in the file f.
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


def main():
    '''
    '''
    # Dynamic programming(?)
    inputFile = input() # Should take in a file of filenames of the genes in the same directory as this python file.
    geneFilenames = open(inputFile, 'r')

    # This will contain the Gene objects (for all genes).
    listOfGenes = []

    # Assuming the filenames in geneFilenames are sorted in the same way as the actual files are sorted in the directory.
    i = 0
    for gene in geneFilenames:
        geneSequences = getSequences(gene[:-1]) # Ignoring the '\n' at the end of each filename.
        listOfGenes.append(Gene(i, geneSequences))
        i+=1

    geneFilenames.close()

    # For each gene, we align its sequences to the other
    # genes, and then store the score in its matrix.
    # At the same time, for each of the other genes, we
    # store the score between their sequences and this
    # gene's sequences in their respective matrices. After 
    # a gene has been iterated on we don't include it in
    # the coming alignments to be done for the rest of the
    # genes during the next iterations as its alignment
    # has already been done with them and the scores
    # stored in both their matrices. For genes with only
    # one sequence we store the scores only in the
    # matrices of the genes they're being aligned with
    # (only when they're being iterated on).
    
    repSeqNrList = [] # Representative sequence number list.
    
    # Each iteration of this while-loop will find the representative sequence of a gene
    while len(listOfGenes) > 1: # While listOfGenes has more than 1 gene.
        gene = listOfGenes[0] # get the 1st gene from this list
        listOfGenes = listOfGenes[1:] # Remove gene from the list.
        
        # Constructing the ScoreMatrix for gene
        # And storing the scores of the alignments between gene and the rest in
        # listOfGenes in their respective matrices.
        for gene2 in listOfGenes:
            scores = findScores(gene.sequences, gene2.sequences)
            # An example:
            # gene's scores = [[11,20,35,1],[20,11,10,34],[7,14,36,2]]
            # should be stored in gene2's score matrix like so:
            # [[11,20,7],[20,11,14],[35,10,36],[1,34,2]]
            
            # If gene has more than 1 sequence.
            if len(gene.sequences) > 1:
                # Storing scores in gene's matrix.
                for i in range(len(scores)):
                    gene.matrix[i]+=scores[i] 
                
                    # Storing the scores in gene2's matrix.
                    for j in range(len(scores[0])): # length of gene2's matrix (nr of sequences).
                        gene2.matrix[j].append(scores[i][j])
                
            # If gene only has 1 sequence.
            elif len(gene.sequences) == 1:
                # Only store the scores in gene2's matrix.
                for i in range(len(scores)):
                    for j in range(len(scores[0])):
                        gene2.matrix[j].append(scores[i][j])
            
            # For some case(s) we can't maybe haven't foreseen.
            else:
                print("A gene has less than 1 sequence?")
                

        representativeSequence = getRepSeqFromScores(gene.matrix)

        # Prints the representative sequence of gene.
        # E.g. if the first sequence is the representative
        # then '0' will be printed (0-indexed).
        print(representativeSequence) 

        # Store the representative sequence of each gene in
        # this list.
        repSeqNrList.append(representativeSequence)
        
        # print(listOfGenes[0].matrix)
        
    # Get the representative transcript of the one leftover gene in
    # listOfGenes.
    print(getRepSeqFromScores(listOfGenes[0].matrix))

    # Store the place of the representative sequence in this list.
    repSeqNrList.append(getRepSeqFromScores(listOfGenes[0].matrix))
    
    # Storing the output.
    outputFile = open("output.txt", "w")
    n = 0
    geneFilenames2 = open(inputFile, "r")
    for gene in geneFilenames2:
        outputFile.write(gene[:-1] + "\n" + str(repSeqNrList[n]) + "\n")

    outputFile.close()


    ### Tests

    # Checking the number of sequences of the 15th gene in the current directory
#    print(len(listOfGenes[14].matrix))

def makeGeneDictionary(transcripts):
    '''
    A transcript must be e.g. ">cds_0_ggal\nATGCGA..." or ">cds_0_btaus\nGAGTC"
    '''
    transcriptDict = {}
    for transcript in transcripts:
        transcriptSplit = transcript.split('\n')
        transcriptDict[transcriptSplit[0]] = transcriptSplit[1] # Storing pairs of transcript ID : transcript.
        
    return transcriptDict

def fillScoreMatrices(geneList):
    while len(geneList) > 1: #while there's more than 1 gene in geneList.
        gene = geneList[0]
        geneList = geneList[1:]
        print('Aligning and finding scores.')
        
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
    Input:
        gene_transcripts: dictionary of the gene's transcripts.

    Output:
        the index of the gene's longest transcript.
    '''
    transcripts = list(gene_transcripts.values())
    largestLength = 0
    longest_id = 0
    for i in range(len(transcripts)):
        if len(transcripts[i]) > largestLength:
            largestLength = len(transcripts[i])
            longest_id = i

    return longest_id

def main2():
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
        


if __name__ == '__main__':
    # main()
    main2()


##### Tests

#gene = getSequences('geneEx.fa')
#allSequences = getSequences('all_seq_no_gene.txt')
#scores = findScores(gene[0], gene[0])
#print(scores)

# Gene class #
#geneSequences = getSequences('geneEx.fa')
#geneTest = Gene(0, geneSequences)
#print(geneTest.matrix)
