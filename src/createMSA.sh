echo "Enter the file of the simulations where the longest transcripts and representatives differ: "

read longestNotRepresentatives

echo "Enter the simulation directory: "

read simulationDirectory

for line in $(cat $longestNotRepresentatives)
	do
		echo "Simulation $line" &&
		clustalo -i ${simulationDirectory}/_iteration_${line}_cds/representatives.fa -o ${simulationDirectory}/_iteration_${line}_cds/aligned_rep.fa -v &&
		clustalo -i ${simulationDirectory}/_iteration_${line}_cds/longestTranscripts.fa -o ${simulationDirectory}/_iteration_${line}_cds/aligned_longest.fa -v
	done
