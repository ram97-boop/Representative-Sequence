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
    
    for gene in genes:
        
        cds_file = open(f, 'r')
        line = cds_file.readline()
        
        while line != '': #while we're not at the end of the file.
            if line[-4:] == gene:
                line = cds_file.readline()
                while line[0] != '>': #while we're not at the end of the transcript
                    
                
            line = cds_file.readline()
                
        cds_file.close()    
            
        
# extract_genes('_iteration_001_cds.fasta')

def main():
    input_string = input() # Will take in the file name and the gene names after.
    input_list = input_string.split()
    extract_genes(input_list[0], input_list[1:])
    
    # print(gene_strings)
    
    # print(gene_strings_to_list(gene_strings))
    
if __name__ == "__main__":
    main()