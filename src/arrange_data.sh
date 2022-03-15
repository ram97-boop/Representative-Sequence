# This shell script is used to create a directory for each of the
# .fasta files produced in the e.g. Example/output/small/cds/
# directory of the modified SimSpliceEvol program. Then, the
# .fasta files will be placed in their respective directory.
# This is done before any work is done on the .fasta files
# like e.g. extracting the representatives, the longest
# sequences etc.

# To run this script enter in the command line:
#	bash arrange_data.sh 
# Then enter the directory with the simulated .fasta files
# which is a copied version of SimSpliceEvol2's cds/ directory.

read simulationDirectory

for geneFile in $(ls ${simulationDirectory}/_iteration_*_cds.fasta)
	do
#		echo "$geneFile"
		geneDirectory=$(echo $geneFile | cut -d . -f 1)
		
		mkdir $geneDirectory &&
		mv $geneFile $geneDirectory/

	done
