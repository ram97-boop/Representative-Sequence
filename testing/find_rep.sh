for directory in $(ls -d alternative_transcripts/*cds)
	do
		echo "$directory/representatives.fa $directory/ggal.fa $directory/mdom.fa $directory/mmus.fa $directory/hsap.fa $directory/btaus.fa"
	done
