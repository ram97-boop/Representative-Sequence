for directory in $(ls -d alternative_transcripts/*cds)
	do
		echo "$directory/randomTranscripts.fa $directory/ggal.fa $directory/mdom.fa $directory/mmus.fa $directory/hsap.fa $directory/btaus.fa" |
		python3 rep_transc.py &&
		echo "Random transcripts of $directory selected."
	done
