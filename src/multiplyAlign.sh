for directory in $(ls -d alternative_transcripts/*cds)
	do
		echo "$directory" &&
		echo "Aligning representatives.fa and randomTranscripts.fa" &&
		clustalo -i "$directory/representatives.fa" -o "$directory/aligned_representatives.fa" &&
		clustalo -i "$directory/randomTranscripts.fa" -o "$directory/aligned_randoms.fa"
	done
