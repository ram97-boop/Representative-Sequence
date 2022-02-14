read simulationDirectory

for directory in $(ls -d ${simulationDirectory}/*cds)
	do
		diff -q $directory/longestTranscripts.fa $directory/representatives.fa |
		cut -d _ -f 3
	done
