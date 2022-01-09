#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def extractGenes(f, genes):
    # print(f)
    # print(genes)
    
    fileList = [] #list of the genes in the input file.
    
    for gene in genes:
        
        cdsFile = open(f, 'r')
        line = cdsFile.readline()
        geneDictionary = {}
        
        while line != '': #while we're not at the end of the file.
        
            if line[-5:-1] == gene: #if we're at one of gene's transcripts.
            
                #store the transcript identifier (w/o the "\n").
                transcript_id = line[:-1]
                geneDictionary[transcript_id] = ''
                
                line = cdsFile.readline()
                while line[0] != '>': #while we're not at the end of the transcript
                    geneDictionary[transcript_id] += line[:-1] #store the transcript subsequence.
                    line = cdsFile.readline()
                    
                
            line = cdsFile.readline()
            
        fileList.append(geneDictionary)
                
        cdsFile.close()
    
    return fileList
            
        
def writeGenesToFile(fileList, genes):
    #>cds_0_ggal
    filePrefix_id = 0
    for gene in fileList:
        fileName = genes[filePrefix_id] + '.fa'
        file = open(fileName, 'w')
        
        for transcript_id, transcript in gene.items():
            file.write(transcript_id + '\n')
            file.write(transcript + '\n')
        
        file.close()
        filePrefix_id+=1


def main():
    inputString = input() # Will take in the file name and the gene names after.
    inputList = inputString.split()
    fileList = extractGenes(inputList[0], inputList[1:])
    # print(fileList)
    
    writeGenesToFile(fileList, inputList[1:])
    
    # file = open('_iteration_001_cds.fasta', 'r')
    # ls = []
    # ls.insert(0,file.readline()[:-1])
    # ls.insert(1,file.readline())
    # ls.insert(2,file.readline())
    # print(ls)
    # file.close()
    
if __name__ == "__main__":
    main()
