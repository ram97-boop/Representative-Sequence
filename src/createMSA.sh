# This shell script is for creating MSAs of the representatives and the longest sequences
# respectively in each simulation. It uses the Clustal Omega command line tool.

# To run this enter in the command line:
#	bash createMSA.sh
# Then enter the file containing the simulation numbers, where in those simulations
# not all the longest sequences were selected as representatives. This file is named
# longestNotReps.txt most likely.
# Finally, enter the directory containing the simulations.

echo "Enter the file listing the simulations where the longest transcripts and representatives differ: "

read longestNotRepresentatives

echo "Enter the simulation directory: "

read simulationDirectory

for line in $(cat $longestNotRepresentatives)
	do
		echo "Simulation $line" &&
		clustalo -i ${simulationDirectory}/_iteration_${line}_cds/representatives.fa -o ${simulationDirectory}/_iteration_${line}_cds/aligned_rep.fa -v &&
		clustalo -i ${simulationDirectory}/_iteration_${line}_cds/longestTranscripts.fa -o ${simulationDirectory}/_iteration_${line}_cds/aligned_longest.fa -v
	done
