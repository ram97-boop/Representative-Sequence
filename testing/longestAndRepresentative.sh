for directory in $(ls -d alternative_transcripts/*cds)
	do
		diff -q $directory/longestTranscripts.fa $directory/representatives.fa
	done
