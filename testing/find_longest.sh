for directory in $(ls -d alternative_transcripts/*cds)
	do
		echo "$directory/longestTranscripts.fa $directory/ggal.fa $directory/mdom.fa $directory/mmus.fa $directory/hsap.fa $directory/btaus.fa" |
		python3 rep_transc.py &&
		echo "Longest transcripts of $directory extracted."
	done
