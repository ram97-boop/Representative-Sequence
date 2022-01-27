for directory in $(ls -d alternative_transcripts/*cds)
	do
		diff -q $directory/randomTranscripts.fa $directory/representatives.fa
	done
