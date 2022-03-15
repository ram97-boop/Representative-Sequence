# This shell script is for calculating how many simulations
# have representatives whose MSA has a higher sum-of-pairs
# score than the longest sequences (or vice versa by
# changing the operator in the if-statement from -ge to -le).

# To run this script enter in the command line:
#	bash compare.sh

directoryPrefix=small/_iteration_
directorySuffix=_cds/
number=0

for simulationNumber in $(cat longestNotReps.txt)
	do
		echo "Simulation $simulationNumber" &&
		if [ $(head -n 1 ${directoryPrefix}${simulationNumber}${directorySuffix}sop.txt) -le $(tail -n 1 ${directoryPrefix}${simulationNumber}${directorySuffix}sop.txt) ]
		then
			number=$(expr $number + 1)
		fi
	done

echo $number
