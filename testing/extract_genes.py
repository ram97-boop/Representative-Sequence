#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def extractGenes(f, genes):
    '''
    Input is a file of the genes together with their alternative transcripts
    and a list of the gene names.
    
    Returns a list of dictionaries, which each consist
    of the alternative transcripts of a gene.
    '''
    # print(f)
    # print(genes)
    
    geneList = [] #list of the genes in the input file.
    
    for gene in genes:
        
        cdsFile = open(f, 'r')
        line = cdsFile.readline()
        geneDictionary = {} #dictionary of gene's alternative transcripts.
        
        while line != '': #while we're not at the end of the file.
        
            # print(line[7:-1])
            if line[7:-1] == gene: #if we're at one of gene's transcripts.
            
                #store the transcript identifier (w/o the "\n").
                transcript_id = line[:-1]
                geneDictionary[transcript_id] = ''
                
                line = cdsFile.readline()
                
                try:
                    while line[0] != '>': #while we're not at the end of the transcript
                        geneDictionary[transcript_id] += line[:-1] #store the transcript subsequence.
                        line = cdsFile.readline()
                        
                except IndexError:
                    if line == '': #if we're at the end of the file.
                        pass
                    
                
            line = cdsFile.readline()
            
        geneList.append(geneDictionary)
                
        cdsFile.close()
    
    return geneList
            
        
def writeGenesToFile(geneList, genes, path):
    '''
    For each gene in geneList (and genes), creates a file of its alternative
    transcripts.
    
    Input:
        geneList: list of gene dictionaries (a dictionary of a gene contains
        the gene's alternative transcripts).
    
        genes: a list of the gene names.
        
        path: the path (str) for where to produce and place the resulting files.
    '''
    filePrefix_id = 0
    for gene in geneList:
        fileName = path + genes[filePrefix_id] + '.fa'
        file = open(fileName, 'w')
        
        for transcript_id, transcript in gene.items():
            file.write(transcript_id + '\n')
            file.write(transcript + '\n')
        
        file.close()
        filePrefix_id+=1


def main():
    inputString = input() # Will take in the file-name and the gene-names after.
                            #e.g. "large/_iteration_001_cds/_iteration_001_cds.fasta ggal mdom mmus hsap btaus"
                            
    inputList = inputString.split()
    geneList = extractGenes(inputList[0], inputList[1:])
    # print(geneList)
    
    path = inputList[0][:-24]
    writeGenesToFile(geneList, inputList[1:], path)
    
    # file = open('_iteration_001_cds.fasta', 'r')
    # ls = []
    # ls.insert(0,file.readline()[:-1])
    # ls.insert(1,file.readline())
    # ls.insert(2,file.readline())
    # print(ls)
    # file.close()
    
def main2():
    inputString = input()
    inputList = inputString.split()
    geneList = extractGenes(inputList[0], inputList[1:])
    writeGenesToFile(geneList, inputList[1:], "")
    
if __name__ == "__main__":
    # main()
    main2()