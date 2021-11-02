### OLD ###
### UNFINISHED ###
# Find representative transcript/sequence for each of the gene-files.
# Usage: bash find-rep.sh

# For each gene file
#for gene in *.fa
#	do
#		# Create a file with all the other gene filenames other than the one in $gene.
# 		for otherGene in *.fa
#			do if [ $gene != $otherGene ]
#				then
#					echo $otherGene >> other_genes.txt
#				fi
#			done
#
#		# Find a representative transcript for gene and output it to the file rep_$gene.
#		python3 python_script.py $gene other_genes.txt > rep_"$gene"
#
#	done
###
### NEWEST ###

# E.g. rep_transc returns 2 (2nd transcript is rep.)
$rep_seq=2

# Stores the line numbers of the id line of the representative transcript
# and the id line of the transcript under it in tmp.txt
grep -n peptide gene_file | head -n $(expr $rep_seq + 1) | tail -n 2 | cut -d : -f 1 > tmp.txt 

# Store the line numbers in these variables and then delete tmp.txt
rep_seq_id_line=$(head -n 1) && next_seq_id_line=$(tail -n 1) && rm tmp.txt 

# Retrieve the id line and the transcript of the representative transcript.
head -n $(expr $next_seq_id_line - 1) gene_file | tail -n $(expr $next_seq_id_line - $rep_seq_id_line)
