read simulationDirectory

for geneFile in $(ls ${simulationDirectory}/_iteration_*_cds.fasta)
	do
#		echo "$geneFile"
		geneDirectory=$(echo $geneFile | cut -d . -f 1)
		
		mkdir $geneDirectory &&
		mv $geneFile $geneDirectory/

	done
