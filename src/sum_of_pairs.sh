echo "Enter the simulation directory: "

read simulationDirectory

for simulationNumber in $(cat longestNotReps.txt)
	do
		echo "Simulation $simulationNumber" &&
		echo "${simulationDirectory}/_iteration_${simulationNumber}_cds/aligned_rep.fa" |
		python3 sum_of_pairs.py > ${simulationDirectory}/_iteration_${simulationNumber}_cds/sop.txt &&
		echo "${simulationDirectory}/_iteration_${simulationNumber}_cds/aligned_longest.fa" |
		python3 sum_of_pairs.py >> ${simulationDirectory}/_iteration_${simulationNumber}_cds/sop.txt
	done
