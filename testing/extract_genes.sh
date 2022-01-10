#testing

for directory in $(ls -d alternative_transcripts/*cds)
	do
		echo "$directory/$(ls $directory) ggal mdom mmus hsap btaus" | python3 extract_genes.py 
	done
