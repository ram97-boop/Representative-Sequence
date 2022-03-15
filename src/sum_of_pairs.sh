# This shell script is for creating a file containing the
# sum-of-pairs scores of the representatives' MSAs and the 
# longest sequences' MSAs respectively of a gene in a
# simulation. This is done for all simulations in the
# input simulation directory. Note that the scoring scheme
# is defined in a function in the sum_of_pairs.py script,
# which is used here.

# To run this script enter in the command line:
#	bash sum_of_pairs.sh
# Then enter the directory containg the simulations.

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
