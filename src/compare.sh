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
