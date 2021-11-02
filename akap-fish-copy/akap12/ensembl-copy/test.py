# -*- coding: utf-8 -*- 

def getSequences(geneFile):
    '''
    Returns a list of the sequences in
    geneFile.
    '''
    gene = open(geneFile, 'r')
    line = gene.readline()
    sequences = [] # Will contain the sequences of gene.
    try:
        seq_i=0
        # While we're not at the end of the file
        while line != '':
            # If we're at the identifier line of a sequence
            if line[0] == '>':

                # Add a placeholder for the sequence in
                # the sequence list
                sequences.append('')

                # Go to the next line, which is the start
                # of the sequence
                line = gene.readline()

                # While we're not at the end of the sequence
                while line != '\n':

                    # Append the line of subsequence without
                    # the '\n' at the end
                    if line[-1] == '\n':
                        sequences[seq_i] += line[:-1]
                    else:
                        sequences[seq_i] += line

                    line = gene.readline()
                
                # line = '\n' so we move to next line
                # which will start with '>'
                line = gene.readline()

                seq_i += 1
    except:
        print('Something went wrong')

    gene.close()
    return sequences


def main():
    pass

#if __name__ == '__main__':
#    main()
