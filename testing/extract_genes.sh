read simulationDirectory

for directory in $(ls -d ${simulationDirectory}/*cds)
	do
		echo "$directory/$(ls $directory) ppan ptro hsap ggor pabe" | python3 extract_genes.py 
#		echo "$(ls $directory/*.fasta) btaus" | python3 extract_genes.py && echo "$directory"
		echo "$(ls $directory/*.fasta)"
	done
