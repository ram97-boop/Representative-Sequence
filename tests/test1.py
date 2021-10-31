# -*- coding: utf-8 -*- 

def readFile(f):
    geneFile = open(f, 'r')
    sequences = geneFile.read()

    # Since the gene file names are unique
    # we print it above the gene's sequences.
    print('fileName: ' + f[:-3] +'\n' +  sequences)
    geneFile.close()

def lookAtOtherGenes(geneFile, seqFile):
    genes = open(geneFile, 'r')

    for gene in genes:
        print(gene)
        sequences = open(seqFile, 'r')
        for seq in sequences:
            if seq == gene:
                print(seq)
                print(gene)

def main():
    f = 'gene.fa'
    readFile(f)

#if __name__ == '__main__':
#    main()
