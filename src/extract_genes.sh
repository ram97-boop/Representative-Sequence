# This shell script is for creating a gene file for each gene
# in a simulation, and each file contains the gene's alternative
# sequences. This is done for all the simulations in the
# simulation directory. Note that the simulations must all have
# the same genes in order for this script to work.

# To run this script enter in the command line:
#	bash extract_genes.sh
# Then enter the directory containing the simulations.

read simulationDirectory

for directory in $(ls -d ${simulationDirectory}/*cds)
	do
		echo "$directory/$(ls $directory) ppan ptro hsap ggor pabe" | python3 extract_genes.py 
#		echo "$(ls $directory/*.fasta) btaus" | python3 extract_genes.py && echo "$directory"
		echo "$(ls $directory/*.fasta)"
	done
