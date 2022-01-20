#testing

for directory in $(ls -d alternative_transcripts/*cds)
	do
		#echo "$directory/$(ls $directory) ggal mdom mmus hsap btaus" | python3 extract_genes.py 
		echo "$(ls $directory/*.fasta) btaus" | python3 extract_genes.py && echo "$directory"
		#echo "$(ls $directory/*.fasta)"
	done
