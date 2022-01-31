read simulationDirectory

for directory in $(ls -d ${simulationDirectory}/*cds)
	do
		echo "$directory/representatives.fa $directory/ppan.fa $directory/ptro.fa $directory/hsap.fa $directory/ggor.fa $directory/pabe.fa" |
		python3 rep_transc.py &&
		echo "Representatives for $directory extracted."
	done
