# Put all the contents of the files in one file
# with the file name above its own contents.
for gene in *.fa
	do
		echo $gene >> all_genes.txt
		cat $gene >> all_genes.txt
	done
