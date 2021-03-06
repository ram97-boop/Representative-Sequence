# Representative-Sequence

### SimSpliceEvol/
Contains the source code of the SimSpliceEvol program at the time of this project. Taken from https://github.com/UdeS-CoBIUS/SimSpliceEvol.

### SimSpliceEvol_modified/
Contains the modifications to the original source code of SimSpliceEvol. The modifications is for making the program produce five alternative sequences per gene in a simulation. 

### src/small/
Contains 500 simulations created by using SimSpliceEvol_modified with the default options, and with the small.nw input guide tree. These simulations are what our algorithm is tested on.

In each directory here, there is the .fasta file that was produced by the modified SimSpliceEvol program, and there are the gene files with the .fa suffix, e.g. hsap.fa, which were extracted from the .fasta file. There is also the representatives.fa file containing the genes' representatives selected by the algorithm in the rep_transc.py script, and there is the longestTranscripts.fa containing the genes' longest sequences.

### src/SimSpliceEvol_testRun/
Contains 100 simulations created by using SimSpliceEvol_modified with the large.nw input guide tree. These simulations were just an initial test run. What could be interesting here is that, while SimSpliceEvol_modified is modified to produce strictly five sequences per gene in a simulation, some simulations here have empty sequences, i.e. there is a sequence identifier and then an empty line. Look at the src/SimSpliceEvol_testRun/_iteration_100_cds/_iteration_100_cds.fasta file for example. This could be because of the program simulating evolutionary events like e.g. exon loss to the point where there is nothing of the sequence left anymore. Especially with the large input tree causing more evolutionary events along its branches.

### src/
The shell scripts in src/ each contain documentation for what and how it is used. The functions defined in the python scripts all contain documentation as well. Most notably, the functions fillScoreMatrices() and findScores() defined in rep_transc.py are the ones that pairwisely aligns, for each gene in the input, the gene's alternative sequences with the other genes' sequences, and it stores the alignment scores in the genes' respective score matrices. The function getRepSeqFromScores() is what finds the representatives of each gene.
