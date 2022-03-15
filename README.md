# Representative-Sequence

### SimSpliceEvol/
Contains the source code of the SimSpliceEvol program at the time of this project.

### SimSpliceEvol_modified/
Contains the modifications to the original source code of SimSpliceEvol. The modifications is for making the program produce five alternative transcripts per gene in a simulation. 

### src/small/
Contains 500 simulations created by using SimSpliceEvol_modified with the default options, and with the small.nw input guide tree.

The shell scripts in src/ each contain documentation for what and how it are used. The functions defined in the python scripts all contain documentation as well. The functions fillScoreMatrices() and findScores() defined in rep_transc.py are the ones that pairwisely aligns, for each gene in the input, the gene's alternative sequences with the other genes' sequences, and it stores the alignment scores in the genes' respective score matrices. The function getRepSeqFromScores() is what finds the representatives of each gene.
