#testing testing

#n=1
for geneFile in $(ls _iteration_*_cds.fasta)
	do
		geneDirectory=$(echo $geneFile | cut -d . -f 1)
		
		mkdir $geneDirectory &&
		mv $geneFile $geneDirectory/

#		echo $n
#		n=$(expr $n + 1)
	done
