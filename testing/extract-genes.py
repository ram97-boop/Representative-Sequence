#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def gene_strings_to_list(genes_string):
    '''
    Input: A string of the gene names seperated by a space in between,
    e.g. "ggal mdom mmus"
    
    Output: A list of the gene names,
    e.g. ["ggal", "mdom", "mmus"]
    '''
    return genes_string.split()

def extract_genes(f, genes):
    # print(f)
    # print(genes)
    
    file_list = [] #will hold, for each gene, a dictionary of transcript_id : transcript sequence.
    
    for gene in genes:
        
        cds_file = open(f, 'r')
        line = cds_file.readline()
        gene_dict = {}
        
        while line != '': #while we're not at the end of the file.
        
            if line[-4:] == gene: #if we're at one of gene's transcripts.
            
                #store the transcript identifier (w/o the "\n").
                transcript_id = line[:-1]
                gene_dict[transcript_id] = ''
                
                line = cds_file.readline()
                while line[0] != '>': #while we're not at the end of the transcript
                    gene_dict[transcript_id] += line[:-1] #store the transcript subsequence.
                    line = cds_file.readline()
                
            line = cds_file.readline()
            
        file_list.append(gene_dict)
                
        cds_file.close()
    
    return file_list
            
        
# extract_genes('_iteration_001_cds.fasta')

def main():
    input_string = input() # Will take in the file name and the gene names after.
    input_list = input_string.split()
    file_list = extract_genes(input_list[0], input_list[1:])
    print(file_list)
    
    # file = open('_iteration_001_cds.fasta', 'r')
    # ls = []
    # ls.insert(0,file.readline()[:-1])
    # ls.insert(1,file.readline())
    # ls.insert(2,file.readline())
    # print(ls)
    # file.close()
    
if __name__ == "__main__":
    main()